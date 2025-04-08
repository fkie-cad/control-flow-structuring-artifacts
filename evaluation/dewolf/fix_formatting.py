import json
import base64
import subprocess
import tempfile
import tqdm

def apply_astyle(code):
    try:
        with tempfile.NamedTemporaryFile(mode='w+', suffix='.c', delete=True) as tmp:
            tmp.write(code)
            tmp.flush()
            
            subprocess.run(['astyle', tmp.name])
            
            with open(tmp.name, 'r') as f:
                return f.read()
    except: return code

def process_file(filename):
    modified_lines = []
    
    with open(filename, 'r') as f:
        lines = f.readlines()
        
    for line in tqdm.tqdm(lines):
        result = json.loads(line)
        if result['decompiler_output']:
            decoded = base64.b64decode(result['decompiler_output']).decode('utf-8')
            formatted = apply_astyle(decoded)
            result['decompiler_output'] = base64.b64encode(formatted.encode()).decode()
        modified_lines.append(json.dumps(result))
    
    with open(filename, 'w') as f:
        for line in modified_lines:
            print(line, file=f)

if __name__ == '__main__':
    process_file('dewolf/results_dewolf.json')