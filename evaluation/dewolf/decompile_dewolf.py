import json
import base64
import sys
import os
import time
import multiprocessing
import git
import tqdm

from pebble import ProcessPool, ProcessExpired
from concurrent.futures import TimeoutError

DEWOLF_PATH = "../../../dewolf"
MALPEDIA_PATH = "../../../malpedia"
OUTPUT_FILE = "results_dewolf.json"
TIMEOUT_SECONDS = 5 * 60

repo = git.Repo(DEWOLF_PATH)
DEWOLF_VERSION = repo.head.object.hexsha

sys.path.append(DEWOLF_PATH)
from decompile import Decompiler


def load_existing_results(output_file):
    processed = set()
    if os.path.exists(output_file):
        with open(output_file, 'r') as f:
            for line in f:
                result = json.loads(line.strip())
                processed.add(f"{result['binary_path']}_{result['function_address']}")
    return processed    

def decompile_with_timeout(filepath, function_address):
    start_time = time.time()
    try:
        decompiler = Decompiler.from_path(filepath)
        _, code = decompiler.decompile(function_address)
        elapsed_time = time.time() - start_time
        return code, elapsed_time
    except Exception as e:
        return None, str(e)

def decompile_all_functions_in_dataset(path):
    processed_functions = load_existing_results(OUTPUT_FILE)
    
    with open(path, "r") as infile:
        all_functions = json.load(infile)
    
    with ProcessPool(max_workers=multiprocessing.cpu_count()) as pool:
        with open(OUTPUT_FILE, "a") as outfile:
            for function in tqdm.tqdm(all_functions):
                function_key = f"{function['malpedia_path']}_{function['function_address']}"
                if function_key in processed_functions:
                    continue
                    
                filepath = os.path.join(MALPEDIA_PATH, function["malpedia_path"])

                result = {
                    "decompiler": "dewolf",
                    "decompiler_version": DEWOLF_VERSION,
                    "binary_sha256": function["binary_sha256"],
                    "packed_sha256": function["packed_sha256"],
                    "binary_path": function["malpedia_path"],
                    "function_address": function["function_address"],
                    "num_blocks": function["num_blocks"],
                    "time_in_seconds": 0,
                    "decompiler_output": "",
                    "error": None,
                    "timeout": False
                }
                
                try:
                    future = pool.schedule(
                        decompile_with_timeout,
                        args=(filepath, function["function_address"]),
                        timeout=TIMEOUT_SECONDS
                    )
                    
                    decompiler_output, elapsed_time = future.result()
                    
                    if decompiler_output is not None:
                        result["decompiler_output"] = base64.standard_b64encode(decompiler_output.encode("utf-8")).decode("ascii")
                        result["time_in_seconds"] = elapsed_time
                    
                except (TimeoutError, ProcessExpired) as error:
                    result["error"] = str(error)
                    result["timeout"] = True
                    result["time_in_seconds"] = TIMEOUT_SECONDS
                
                json.dump(result, outfile)
                outfile.write("\n")
                outfile.flush()
    

if __name__ == "__main__":
    decompile_all_functions_in_dataset("dataset/stratified_dataset_functions.json")
