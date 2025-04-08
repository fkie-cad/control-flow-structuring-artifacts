import base64
import glob
import json
import os
import re
import subprocess
import tempfile

import pyjoern
import tqdm
from pebble import ProcessPool

PATH_TO_RESULTS = "../**/results_*.json"

def apply_astyle(code):
    try:
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.c', delete=True) as tmp:
            tmp.write(code)
            tmp.flush()
            subprocess.run(['astyle', tmp.name], stdout=subprocess.DEVNULL)
            with open(tmp.name, 'r') as f:
                return f.read()
    except: return code

def clean_decompiler_output(decompiler_output, identifier):
    try:
        result = re.search(r'^[^{]*\)[\sa-zA-Z_]*{', decompiler_output, flags=re.MULTILINE)

        cleaned = "int test()" + decompiler_output[result.end()-1:]
        cleaned = re.sub(r'^\s*$\n', '', cleaned, flags=re.MULTILINE)
        cleaned = apply_astyle(cleaned)
        return cleaned
    except: 
        print(f"ERROR: Cleanup failed for {identifier}")        
        return decompiler_output
    
def calculate_cyclomatic_complexity(relevant_function):
    e = len(list(relevant_function.cfg.edges))
    n = len(list(relevant_function.cfg.nodes))
    cc = e - n + 2
    return cc

def extract_metric_from_results(function_results_raw):
    function_results = json.loads(function_results_raw)
    if not function_results['decompiler_output']: return None

    decoded_source = base64.standard_b64decode(function_results['decompiler_output']).decode("utf-8").strip()
    decoded_lines = decoded_source.split("\n")

    if decoded_source in ["TimeOut", "Error during Decompilation", "No decompilation Output!"]: return None
    elif decoded_lines[-1] in ["TimeOut", "Error during Decompilation", "Function not found in decompiler output!"]: return None
    elif function_results['decompiler'] == "dewolf" and (len(decoded_lines) >= 2 and decoded_lines[-2] == "Decompilation Failed!"): return None

    with tempfile.NamedTemporaryFile(mode='w+', delete=True, suffix='.c') as temp_file:
        identifier = f"{function_results['decompiler']}_{function_results['binary_path']}_{function_results['function_address']}"
        temp_file.write(clean_decompiler_output(decoded_source, identifier=identifier))
        temp_file.flush()
        try:
            functions = pyjoern.parse_source(temp_file.name)
            relevant_function = functions["test"]
        except:
            print(f"Failed to parse {identifier}")
            return {}
        
        cyclomatic_compplexity = calculate_cyclomatic_complexity(relevant_function)
        if cyclomatic_compplexity < 2:
            print(f"WARNING: Low Cyclomatic Complexity for {identifier}")

        return {
            "decompiler": function_results['decompiler'],
            "decompiler_version": function_results['decompiler_version'],
            "binary_path": function_results['binary_path'],
            "function_address": function_results['function_address'],
            "num_blocks": function_results['num_blocks'],
            "num_gotos": len(relevant_function.gotos),
            "cyclomatic_complexity": cyclomatic_compplexity,
            "lines_of_code": relevant_function.end_line - relevant_function.start_line + 1,
        }
        

def process_results_files():
    for file_path in glob.glob(PATH_TO_RESULTS, recursive=True):
        decompiler_name = file_path.split('_')[1].split('.')[0]
        output_file = f"metrics_{decompiler_name}.json"
        if os.path.exists(output_file): continue
        with open(file_path, 'r') as f:
            print(f"Started Processing: {file_path}")
            with open(output_file, 'w') as outfile:
                with ProcessPool(max_workers=4) as pool:
                    future = pool.map(extract_metric_from_results, f.readlines())
                    for sample_function_results in tqdm.tqdm(future.result(), total=1000, smoothing=0):
                        print(json.dumps(sample_function_results), file=outfile)
                        outfile.flush()

if __name__ == "__main__":
    process_results_files()