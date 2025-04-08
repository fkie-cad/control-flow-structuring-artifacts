import base64
import datetime
import json
import re
import subprocess
from pathlib import Path

from parse_data_set import parse_data

TIMEOUT = 5 * 60  # 5 minutes


def get_decompiler_version():
    try:
        version = subprocess.run("source ./environment && revng --version", shell=True, capture_output=True, check=True)
        return str(version.stdout.strip(), "utf-8")
    except Exception:
        return "No version found"

def get_single_function(decompiled_file: Path, start_string: str, end_string: str):
    try:
        with open(decompiled_file, "r") as f:
            in_function = False
            function_lines = []
            brace_count = 0

            for line in f:  # Iterate over lines directly from the file

                if re.search(start_string, line):
                    in_function = True

                if not in_function:
                    continue

                function_lines.append(line)
                brace_count += line.count("{") - line.count("}")

                if line.startswith(end_string) and brace_count == 0:
                    return "".join(function_lines)

                if line.startswith(end_string) or brace_count == 0:
                    print(f"Check function {decompiled_file} - {start_string}")
                    return "".join(function_lines)

            return "Function not found in decompiler output!"
    except FileNotFoundError:
        print(f"Error: File '{decompiled_file}' not found.")
        return "Error during Decompilation"
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error during Decompilation"


def decompile_all_functions():

    decompiler_version = get_decompiler_version()
    output_file = Path(f"results_revngc.json")

    if output_file.is_file():
        output_file.unlink()

    with open(output_file, "a") as f:
        for function in parse_data():
            try:
                output_path = Path(f"output_{function.binary_sha}_{function.address:x}.c")
                start_time = datetime.datetime.now()
                result = subprocess.run(
                    f"./decompile_revng_c.sh {function.path} {output_path}",
                    shell=True,
                    capture_output=True,
                    timeout=TIMEOUT,
                    check=True,
                )
                end_time = datetime.datetime.now()
                decompiled_code = get_single_function(output_path, rf"function_{hex(function.address)}_[^\n]*{{", "}")
                time = str((end_time - start_time).total_seconds())

            except subprocess.TimeoutExpired:
                decompiled_code = "TimeOut"
                time = "inf"
                print(f"Timeout during decompilation of: {function.path} - {function.address}")

            except Exception:
                decompiled_code = "Error during Decompilation"
                time = "inf"
                print(f"Error during decompilation of: {function.path} - {function.address}")

            result_data = {
                "decompiler": "revng-c",
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
