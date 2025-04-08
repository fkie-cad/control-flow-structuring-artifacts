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
        result = subprocess.run("r2pm -gi", shell=True, text=True, capture_output=True, check=True)

        # Regular expression to match the version information
        match = re.search(r"INFO: Using (r2-\d+\.\d+\.\d+) and (r2pm-\d+\.\d+\.\d+)", result.stderr)

        if match:
            r2_version = match.group(1)
            r2pm_version = match.group(2)
            version = f"{r2_version} - {r2pm_version}"  # Return combined string
        else:
            version = result.stderr  # compelete output

        path_r2dec = subprocess.run("r2pm -U", shell=True, text=True, capture_output=True, check=True)
        # Regex to capture the path
        match = re.search(r"INFO: Running git pull on (.*)", path_r2dec.stderr)

        if match:
            path = match.group(1).strip()  # Remove any leading/trailing whitespace
            r2dec_version = subprocess.run(f"cat {path}/.git/ORIG_HEAD", shell=True, text=True, capture_output=True, check=True)
            version += f" - r2dec-{r2dec_version.stdout}"
        else:
            version += " - no r2dec Version found"  # Or raise an exception
        return version
    except Exception:
        return "No version found"


def decompile_all_functions():

    decompiler_version = get_decompiler_version()
    output_file = Path(f"results_radare.json")

    if output_file.is_file():
        output_file.unlink()

    with open(output_file, "a") as f:
        for function in parse_data():
            try:
                start_time = datetime.datetime.now()
                result = subprocess.run(
                    f"python decompile_single_function.py {function.path} {function.address}",
                    shell=True,
                    capture_output=True,
                    timeout=TIMEOUT,
                    check=True,
                )
                end_time = datetime.datetime.now()
                decompiled_code = result.stdout.decode("utf-8")
                time = str((end_time - start_time).total_seconds())

                with open(Path(f"log_data_{function.binary_sha}_{function.address:x}.log"), "w") as log_file:
                    log_file.write(result.stderr.decode("utf-8"))

            except subprocess.TimeoutExpired:
                decompiled_code = "TimeOut"
                time = "inf"
                print(f"Timeout during decompilation of: {function.path} - {function.address}")

            except Exception:
                decompiled_code = "Error during Decompilation"
                time = "inf"
                print(f"Error during decompilation of: {function.path} - {function.address}")

            result_data = {
                "decompiler": "radare",
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
