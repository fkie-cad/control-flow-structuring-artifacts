import base64
import json
import subprocess
from pathlib import Path
from typing import Literal

import angr

from parse_data_set import parse_data

TIMEOUT = 5 * 60  # 5 minutes


def decompile_all_functions(decompiler: Literal["SAILR", "DREAM", "Phoenix"]):

    output_file = Path(f"results_{decompiler}.json")

    if output_file.is_file():
        output_file.unlink()

    with open(output_file, "a") as f:
        for function in parse_data():
            try:
                result = subprocess.run(
                    f"python decompile_single_function.py {function.path} {function.address} {decompiler}",
                    shell=True,
                    capture_output=True,
                    timeout=TIMEOUT,
                    check=True,
                )
                decompiler_result = json.loads(result.stdout.decode("UTF-8"))
                decompiled_code = decompiler_result["decompiler_output"]
                time = decompiler_result["time"]

            except subprocess.TimeoutExpired:
                decompiled_code = "TimeOut"
                time = "inf"
                print(f"Timeout during decompilation of: {function.path} - {function.address}")

            except Exception:
                decompiled_code = "Error during Decompilation"
                time = "inf"
                print(f"Error during decompilation of: {function.path} - {function.address}")

            result_data = {
                "decompiler": decompiler,
                "decompiler_version": angr.__version__,
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
