import base64
import json
import multiprocessing
import os
import subprocess
import tempfile
import time
from concurrent.futures import TimeoutError

import tqdm
from pebble import ProcessPool, ProcessExpired

GHIDRA_PATH = "PATH_TO_GHIDRA_IMPLEMENTATION"
MALPEDIA_PATH = "../../../malpedia"
OUTPUT_FILE = "results_ghidra.json"
TIMEOUT_SECONDS = 5 * 60
TEMPORARY_DECOMPILER_OUTPUT = os.path.join(tempfile.gettempdir(), "decompiler_output.c")

def load_existing_results(output_file):
    processed = set()
    if os.path.exists(output_file):
        with open(output_file, 'r') as f:
            for line in f:
                result = json.loads(line.strip())
                processed.add(f"{result['binary_path']}_{result['function_address']}")
    return processed    

def create_ghidra_script(function_address):
    return f"""
from ghidra.app.decompiler import DecompInterface
from ghidra.util.task import ConsoleTaskMonitor


decompiler = DecompInterface()
decompiler.openProgram(currentProgram)
function = getFunctionContaining(toAddr({function_address}))
if function is not None:
    print("Decompiling function at {function_address}")
    results = decompiler.decompileFunction(function, 30, ConsoleTaskMonitor())
    if results.decompileCompleted():
        with open("{TEMPORARY_DECOMPILER_OUTPUT}", "w") as f:
            f.write(results.getDecompiledFunction().getC())
else:
    print("Function not found")
"""

def decompile_with_timeout(filepath, function_address):
    start_time = time.time()
    try:
        with tempfile.TemporaryDirectory() as temp_dir:
            project_name = "temp_project"
            script_path = os.path.join(temp_dir, "decompile.py")
            
            with open(script_path, "w") as f:
                f.write(create_ghidra_script(function_address))
            
            cmd = [
                f"{GHIDRA_PATH}/support/analyzeHeadless",
                temp_dir,
                project_name,
                "-import", filepath,
                "-postScript", script_path,
                "-deleteProject"
            ]
            
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            
            stdout, stderr = process.communicate(timeout=TIMEOUT_SECONDS)

            print(stdout)

            try:  
                with open(TEMPORARY_DECOMPILER_OUTPUT, "r") as f:
                    decompiled = f.read()
                if not decompiled: 
                    return None, "Decompilation failed"
            except FileNotFoundError:
                return None, "Decompilation failed, no file created"
            finally:
                os.remove(TEMPORARY_DECOMPILER_OUTPUT)
                
            elapsed_time = time.time() - start_time
            return decompiled.strip(), elapsed_time
            
    except subprocess.TimeoutExpired:
        process.kill()
        return None, "Timeout"
    except Exception as e:
        return None, str(e)

def decompile_all_functions_in_dataset(path):
    processed_functions = load_existing_results(OUTPUT_FILE)
    
    with open(path, "r") as infile:
        all_functions = json.load(infile)
    
    with ProcessPool(max_workers=multiprocessing.cpu_count()) as pool:
        with open(OUTPUT_FILE, "a") as outfile:
            for function in tqdm.tqdm(list((func for func in all_functions if f"{func['malpedia_path']}_{func['function_address']}" not in processed_functions)), smoothing=0):
                    
                filepath = os.path.join(MALPEDIA_PATH, function["malpedia_path"])
                
                result = {
                    "decompiler": "ghidra",
                    "decompiler_version": "11.3.1",
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
                    else:
                        result["error"] = elapsed_time
                    
                except (TimeoutError, ProcessExpired) as error:
                    result["error"] = str(error)
                    result["timeout"] = True
                    result["time_in_seconds"] = TIMEOUT_SECONDS
                
                json.dump(result, outfile)
                outfile.write("\n")
                outfile.flush()
    

if __name__ == "__main__":
    decompile_all_functions_in_dataset("dataset/stratified_dataset_functions.json")
