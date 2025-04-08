import json
import logging
import os
import re
import struct
import sys
import traceback
from collections import defaultdict
from multiprocessing import Pool, cpu_count

import tqdm
from smda.Disassembler import Disassembler

logging.basicConfig(filename="/tmp/smda.log",
                    filemode='a',
                    format='[%(asctime)s:%(msecs)d] %(name)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)

logger = logging.getLogger('smda-multithreaded')
formatter = logging.Formatter('%(process)d - %(processName)s - %(threadName)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)

MALPEDIA_PATH = "../../../malpedia"
DUMP_FILE_PATTERN = re.compile("dump7?_0x[0-9a-fA-F]{8,16}")
UNPACK_FILE_PATTERN = re.compile("_unpacked(_x64)?$")

def get_word(buffer, start):
    return _get_binary_data(buffer, start, 2)


def get_dword(buffer, start):
    return _get_binary_data(buffer, start, 4)


def get_qword(buffer, start):
    return _get_binary_data(buffer, start, 8)


def _get_binary_data(buffer, start, length):
    if length not in _unsigned_unpack_formats:
        raise RuntimeError("Unsupported data length")

    return struct.unpack(_unsigned_unpack_formats[length], buffer[start:start + length])[0]


_unsigned_unpack_formats = {
    2: "H",
    4: "I",
    8: "Q"
}

def get_pe_offset(content):
    if len(content) >= 0x40:
        pe_offset = get_word(content, 0x3c)
        return pe_offset
    raise RuntimeError("Buffer too small to extract PE offset (< 0x40)")


def check_bitness(content):
    bitness = None
    pe_offset = get_pe_offset(content)
    if pe_offset and len(content) >= pe_offset + 6:
        bitness = get_word(content, pe_offset + 4)
        bitness_map = {0x14c: 32, 0x8664: 64}
        bitness = bitness_map[bitness] if bitness in bitness_map else 0
    return bitness


class NativeCodeIdentifier(object):

    def _identifyDotnet(self, content):
        if not check_bitness(content):
            return False
        pe_offset = get_pe_offset(content)
        file_characteristics_offset = pe_offset + 0x18
        file_characteristics = get_word(content, file_characteristics_offset)
        field_offset = 0
        if file_characteristics == 0x10b:
            field_offset = 0xE8
        elif file_characteristics == 0x20b:
            field_offset = 0xF8
        image_dir_com_descriptor_offset = pe_offset + field_offset
        # only .NET binaries will feature a COM dscription in the data directory
        com_descriptor_offset = get_dword(content, image_dir_com_descriptor_offset)
        if field_offset > 0 and len(content) - 8 > com_descriptor_offset > 0:
            return True
        return False

    def _identifyDelphi(self, content):
        # check PE header for typical sections
        if b"CODE" in content[:0x400] and b"DATA" in content[:0x400]:
            return True
        # check CODE for typical Delphi class names
        if b"\x07TObject" in content[:0x2000] or b"\x0AWideString" in content[:0x2000]:
            return True
        return False

    def _identifyGo(self, content):
        # Go binaries always have a build ID in their beginning
        if b"Go build ID:" in content[:0x1400]:
            return True
        return False

    def _identifyPython(self, content):
        if re.search(b"python(2|3).\\.dll", content):
            return True
        return False

    def isNativeCode(self, filepath):
        content = ""
        with open(filepath, "rb") as fin:
            content = fin.read()
        # identify Delphi
        is_delphi = self._identifyDelphi(content)
        # identify Go
        is_go = self._identifyGo(content)
        # identify .NET
        is_dotnet = self._identifyDotnet(content)
        # identify PyInstaller
        is_python = self._identifyPython(content)
        return not (is_delphi or is_go or is_dotnet or is_python)


def parseBaseAddrFromArgs(filename):
    baddr_match = re.search(re.compile("0x(?P<base_addr>[0-9a-fA-F]{8,16})"), filename)
    if baddr_match:
        return int(baddr_match.group("base_addr"), 16)
    return 0


def getBitnessFromFilename(filename):
    baddr_match = re.search(re.compile("0x(?P<base_addr>[0-9a-fA-F]{8,16})"), filename)
    if baddr_match:
        return 32 if len(baddr_match.group("base_addr")) == 8 else 64
    return 0


def readFileContent(file_path):
    file_content = b""
    with open(file_path, "rb") as fin:
        file_content = fin.read()
    return file_content


def getAllReportFilenames(output_path):
    report_filenames = set([])
    for root, subdir, files in os.walk(output_path):
        for filename in files:
            report_filenames.add(filename)
    return report_filenames


def getFamilyName(input_path):
    family_name = ""
    abs_path = os.path.abspath(input_path)
    for folder in abs_path.split("/")[::-1]:
        if folder == "malpedia":
            break
        family_name = folder
    return family_name

def getSampleVersion(input_path, family):
    family_name = ""
    abs_path = os.path.dirname(os.path.abspath(input_path))
    for folder in abs_path.split("/")[::-1]:
        if folder == family or folder == "modules":
            break
        family_name = folder
    return family_name


def getMalpediaFilePath(input_path):
    egg = 'malpedia/'
    abs_path = os.path.abspath(input_path)
    pos = abs_path.index(egg)
    malpedia_filepath = abs_path[pos + len(egg):]
    return malpedia_filepath


def work(input_element):
    if input_element['filename'] + ".smda" in input_element['finished_reports']:
        print("Skipping file {}".format(input_element['filepath']))
        return
    report = None
    input_filepath = input_element['filepath']
    input_filename = input_element['filename']
    identifier = NativeCodeIdentifier()
    if not identifier.isNativeCode(input_filepath):
        return
    malpedia_relative_path = getMalpediaFilePath(input_filepath)
    in_family_path = os.sep.join(malpedia_relative_path.split(os.sep)[1:])
    if in_family_path.startswith("module"):
        return
    disassembler = Disassembler()
    try:
        if "elf." in input_filepath and ("x86" in input_filepath or "x64" in input_filepath) and re.search(UNPACK_FILE_PATTERN, input_element['filename']):
            print("Analyzing file: {}".format(input_filepath))
            try:
                report = disassembler.disassembleFile(input_filepath)
            except AttributeError:
                logger.error("exception for: " + str(input_filename))
        elif "win." in input_filepath and re.search(UNPACK_FILE_PATTERN, input_element['filename']):
            print("Analyzing file: {}".format(input_filepath))
            try:
                report = disassembler.disassembleFile(input_filepath)
            except AttributeError:
                logger.error("AttributeError for: " + str(input_filename))
        elif re.search(DUMP_FILE_PATTERN, input_element['filename']):
            print("Analyzing file: {}".format(input_filepath))
            BUFFER = readFileContent(input_filepath)
            BASE_ADDR = parseBaseAddrFromArgs(input_filename)
            BITNESS = getBitnessFromFilename(input_filename)
            try:
                report = disassembler.disassembleBuffer(BUFFER, BASE_ADDR, BITNESS)
            except AttributeError:
                logger.error("AttributeError for: " + str(input_filename))
        if report:
            report.family = getFamilyName(input_filepath)
            report.version = getSampleVersion(input_filepath, report.family)
            report.filename = os.path.basename(malpedia_relative_path)
            with open(input_element['output_path'] + os.sep + input_filename + ".smda", "w") as fout:
                json.dump(report.toDict(), fout, indent=1, sort_keys=True)
                logger.info("Wrote " + str(input_element['output_path'] + os.sep + input_filename) + ".smda")
    except Exception:
        print("RunTimeError, we skip!")
        print("smda: " + str( input_filename ))
        traceback.print_exc()
    return None


if __name__ == "__main__":
    if not os.path.exists("smda-malpedia"):
        os.makedirs("smda-malpedia")
    finished_reports = getAllReportFilenames("smda-malpedia")
    input_queue = []

    # Find all targets (everything) to disassemble in malpedia.
    for root, subdir, files in sorted(os.walk(MALPEDIA_PATH)):
        if ".git" in root:
            continue
        for filename in sorted(files):
            if not (re.search(UNPACK_FILE_PATTERN, filename) or re.search(DUMP_FILE_PATTERN, filename)):
                continue
            filepath = root + os.sep + filename
            input_element = {
                "filename": filename,
                "finished_reports": finished_reports,
                "filepath": filepath,
                "output_path": "smda-malpedia",
                "malpedia_path": MALPEDIA_PATH
            }
            input_queue.append(input_element)

    results = []
    with Pool(12) as pool:
        for result in tqdm.tqdm(pool.imap_unordered(work, input_queue), total=len(input_queue)):
            results.append([result])
