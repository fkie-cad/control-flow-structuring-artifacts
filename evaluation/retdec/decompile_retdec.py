import base64
import datetime
import json
import subprocess
from pathlib import Path

from parse_data_set import parse_data

TIMEOUT = 5 * 60  # 5 minutes


def get_decompiler_version():
    try:
        result = subprocess.run("bin/retdec-decompiler --version", shell=True, capture_output=True, check=True)
        version_data = result.stdout.decode("utf-8").split("\n")
        return f"{version_data[0]} - {version_data[1]}"
    except:
        return "No version found"


def get_decompiled_code(filepath: Path):
    try:
        with open(filepath, "r") as f:
            retdec_output = f.readlines()
    except Exception as e:
        print(f"Error while parsing the decompiled code: {e}")
        return "Error during Decompilation!"

    if retdec_output[-2] != "// Detected functions: 1\n":
        return f"Function not found in decompiler output!"

    start_marker = "// ------------------------ Functions -------------------------\n"
    end_marker_pattern = r"// ----------------"

    start_idx = 0
    end_idx = 0
    for idx, line in enumerate(retdec_output):
        if start_idx == 0 and line == start_marker:
            start_idx = idx
        elif start_idx > 0 and line.startswith(end_marker_pattern):
            end_idx = idx
            break

    if start_idx == 0 or end_idx == 0:
        return f"Function not found in decompiler output!"  # Markers not found

    return "".join(retdec_output[i] for i in range(start_idx + 3, end_idx - 1))


def decompile_all_functions():

    decompiler_version = get_decompiler_version()
    output_file = Path(f"results_retdec.json")

    if output_file.is_file():
        output_file.unlink()

    with open(output_file, "a") as f:
        for function in parse_data():
            try:
                output_file = Path(f"output_{function.binary_sha}_{function.address:x}.c")
                start_time = datetime.datetime.now()
                result = subprocess.run(
                    f"bin/retdec-decompiler -k {function.path} --select-ranges 0x{function.address:x}-0x{function.address:x} -o {output_file}",
                    shell=True,
                    capture_output=True,
                    timeout=TIMEOUT,
                    check=True,
                )
                end_time = datetime.datetime.now()
                decompiled_code = get_decompiled_code(output_file)
                time = str((end_time - start_time).total_seconds())

                with open(Path(f"log_data_{function.binary_sha}_{function.address:x}.log"), "w") as log_file:
                    log_file.write(result.stdout.decode("utf-8"))

            except subprocess.TimeoutExpired:
                decompiled_code = "TimeOut"
                time = "inf"
                print(f"Timeout during decompilation of: {function.path} - 0x{function.address:x}")

            except Exception as e:
                decompiled_code = "Error during Decompilation"
                time = "inf"
                print(f"Error during decompilation of {function.path} - 0x{function.address:x} : {e}")

            result_data = {
                "decompiler": "retdec",
                "decompiler_version": decompiler_version,
                "binary_sha256": function.binary_sha,
                "packed_sha256": function.packed_sha,
                "binary_path": str(function.path).split("malpedia/")[1],
                "function_address": hex(function.address),
                "num_blocks": function.basic_block_number,
                "time_in_seconds": time,
                "decompiler_output": base64.standard_b64encode(decompiled_code.encode("utf-8")).decode("ascii"),
            }

            json.dump(result_data, f)
            f.write("\n")  # Newline after each JSON object
            f.flush()


if __name__ == "__main__":
    decompile_all_functions()
