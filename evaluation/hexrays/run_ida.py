from headless_ida import HeadlessIda
import pathlib
import json
import base64
import time
import sys

IDA_PATH = pathlib.Path("PATH_TO_IDA_IMPLEMENTATION")
MALPEDIA_PATH = pathlib.Path("../../../malpedia")
OUTPUT_DIR = pathlib.Path("output_files")

def get_metadata():
    res = {}
    with pathlib.Path("stratified_dataset_functions.json").open("r") as f:
        data = json.load(f)
        for item in data:
            res[(item['malpedia_path'], item["function_address"])] = item
    return res

def decompile_file(filename: str, offset: int) -> None:
    item = get_metadata().get((filename, hex(offset)))
    filename = MALPEDIA_PATH / filename
    result = {
        "decompiler": "hexrays",
        "decompiler_version": "8.3",
        "binary_sha256": item["binary_sha256"],
        "packed_sha256": item["packed_sha256"],
        "binary_path": item["malpedia_path"],
        "function_address": item["function_address"],
        "num_blocks": item["num_blocks"],
        "time_in_seconds": 0,
        "decompiler_output": "",
        "error": None,
        "timeout": False
    }

    start = time.time()
    headlessida = HeadlessIda(IDA_PATH, str(filename))

    # Import IDA modules after initialization
    import idautils
    import ida_name
    import idaapi

    for func in idautils.Functions():
        if func == offset:
            function = idaapi.get_func(func)
            cfunc = idaapi.decompile(function)
            end = time.time()
            if cfunc is not None:
                decompiled_code = str(cfunc)
                result["decompiler_output"] = base64.standard_b64encode(decompiled_code.encode("utf-8")).decode("ascii")
                result["time_in_seconds"] = end - start
            else:
                result["error"] = "Decompilation failed"
            outfile = OUTPUT_DIR / f"{result['binary_sha256']}_{hex(offset)}.json"
            with pathlib.Path(outfile).open('w') as f:
                json.dump(result, f, indent=4)
            break


if __name__ == "__main__":
    decompile_file(sys.argv[1], int(sys.argv[2], 16))
