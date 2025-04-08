import json
from pathlib import Path
import subprocess

OUTPUT_DIR = Path("output_files")
RESULTS = Path("results_hexrays.json")
DATASET_PATH = Path("../dataset/stratified_dataset_functions.json")

def decompile_all_functions():
    if not OUTPUT_DIR.is_dir():
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(DATASET_PATH, "r") as json_data:
        try:
            function_list = json.load(json_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON file: {e}")
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File '{DATASET_PATH}' not found.")

    for function in function_list:
        file_name = function.get("malpedia_path", "")
        address = int(function.get("function_address", ""), 16)
        subprocess.run(f"python run_ida.py {file_name} {address}", shell=True)


def normalize_dataset(destination_path: Path, dataset_path: Path):
    results = {}
    for result_path in OUTPUT_DIR.iterdir():
        with open(result_path, "r") as f:
            result = json.load(f)
            results[f"{result['binary_sha256']}_{result['function_address']}"] = result

    with open(dataset_path, "r") as f:
        all_functions = json.load(f)

    with open(destination_path, "w") as f:
        for function in all_functions:
            key = f"{function['binary_sha256']}_{function['function_address']}"
            if key in results:
                if results[key]["time_in_seconds"] < 300:
                    print(json.dumps(results[key]), file=f)
                else:
                    print(json.dumps({
                        "decompiler": "hexrays",
                        "decompiler_version": "8.3",
                        "binary_sha256": function["binary_sha256"],
                        "packed_sha256": function["packed_sha256"],
                        "binary_path": function["malpedia_path"],
                        "function_address": function["function_address"],
                        "num_blocks": function["num_blocks"],
                        "time_in_seconds": 300,
                        "decompiler_output": "",
                        "error": "Timeout",
                        "timeout": True
                    }), file=f)
            else:
                print(json.dumps({
                    "decompiler": "hexrays",
                    "decompiler_version": "8.3",
                    "binary_sha256": function["binary_sha256"],
                    "packed_sha256": function["packed_sha256"],
                    "binary_path": function["malpedia_path"],
                    "function_address": function["function_address"],
                    "num_blocks": function["num_blocks"],
                    "time_in_seconds": None,
                    "decompiler_output": "",
                    "error": "No output Generated",
                    "timeout": False
                }), file=f)


if __name__ == "__main__":
    decompile_all_functions()
    normalize_dataset(RESULTS, DATASET_PATH)
