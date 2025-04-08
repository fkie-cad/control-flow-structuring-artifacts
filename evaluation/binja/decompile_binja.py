import os
import json
import base64
import os
import time
import multiprocessing
import tqdm
import binaryninja

from pebble import ProcessPool, ProcessExpired
from concurrent.futures import TimeoutError

MALPEDIA_PATH = "../../../malpedia"
BINJA_VERSION = binaryninja.core_version()
OUTPUT_FILE = "results_binja.json"
TIMEOUT_SECONDS = 5 * 60

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
    bv = None
    settings = binaryninja.DisassemblySettings() 
    settings.set_option(binaryninja.DisassemblyOption.ShowAddress, False) 
    settings.set_option(binaryninja.DisassemblyOption.WaitForIL, True) 
    try:
        if isinstance(function_address, str):
            function_address = int(function_address, 16 if '0x' in function_address else 10)
        address = int(function_address)
    
        bv = binaryninja.load(filepath)
        obj = binaryninja.LinearViewObject.language_representation(bv, settings) 
        cursor = binaryninja.LinearViewCursor(obj) 

        func = bv.get_function_at(address)
        if not func: return None, f"No function found at address {hex(address)}"

        cursor.seek_to_address(func.highest_address) 
        body = bv.get_next_linear_disassembly_lines(cursor) 
        cursor.seek_to_address(func.highest_address) 
        header = bv.get_previous_linear_disassembly_lines(cursor) 
        pseudo_c = "\n".join(str(line.contents) for line in header + body).strip()
            
        # signature = f"{str(func.return_type)} {func.name}({', '.join([f'{str(param.type)} {param.name}' for param in func.parameter_vars])})"
        # full_output = f"{signature}\n{str(func.hlil)}"
        
        elapsed_time = time.time() - start_time
        return pseudo_c, elapsed_time
        
    except Exception as e:
        return None, str(e)
    finally:
        try:
            if bv: bv.file.close()
        except:
            pass

def decompile_all_functions_in_dataset(path):
    processed_functions = load_existing_results(OUTPUT_FILE)
    
    with open(path, "r") as infile:
        all_functions = json.load(infile)
    
    with ProcessPool(max_workers=multiprocessing.cpu_count()) as pool:
        with open(OUTPUT_FILE, "a") as outfile:
            for function in tqdm.tqdm(list((func for func in all_functions if f"{func['malpedia_path']}_{func['function_address']}" not in processed_functions)), smoothing=0):
                   
                filepath = os.path.join(MALPEDIA_PATH, function["malpedia_path"])

                result = {
                    "decompiler": "binja",
                    "decompiler_version": BINJA_VERSION,
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
