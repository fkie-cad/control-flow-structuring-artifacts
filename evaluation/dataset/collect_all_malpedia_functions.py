import os
import zipfile
import tempfile
import json
from io import BytesIO
from smda.common.SmdaReport import SmdaReport
from tqdm import tqdm

def process_smda_reports(base_dir, output_file):
    all_functions = list()
    
    # Count total zip files first
    total_files = sum(1 for _, _, files in os.walk(base_dir) 
                     for f in files if f.endswith('.zip'))
    
    # Main progress bar for files
    with tqdm(total=total_files, desc="Processing SMDA reports") as pbar:
        for root, dirs, files in os.walk(base_dir):
            for filename in files:
                if filename.endswith('.zip'):
                    file_path = os.path.join(root, filename)
                
                    # Load ZIP into memory
                    with open(file_path, 'rb') as f:
                        zip_data = BytesIO(f.read())
                    
                    # Open ZIP in memory
                    with zipfile.ZipFile(zip_data) as zip_ref:
                        smda_files = [f for f in zip_ref.namelist() if f.endswith('.smda')]
                        
                        if not smda_files:
                            print(f"No SMDA file found in {filename}")
                            pbar.update(1)
                            continue
                        
                        # Create temporary file
                        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                            with zip_ref.open(smda_files[0]) as smda_file:
                                temp_file.write(smda_file.read())
                            
                            try:
                                report = SmdaReport.fromFile(temp_file.name)
                                functions = list(report.getFunctions())
                                
                                # Inner progress bar for functions
                                for current_function in tqdm(functions, 
                                                          desc=f"Processing {filename}", 
                                                          leave=False):
                                    all_functions.append((report.filename, 
                                                       hex(current_function.offset), 
                                                       current_function.num_blocks))
                                    
                            except:
                                print(f"Error: Could not load report from {filename}")
                            
                        os.unlink(temp_file.name)
                    pbar.update(1)
                    
    with open(output_file, "w") as jsonfile:
        json.dump(all_functions, jsonfile)

if __name__ == "__main__":
    process_smda_reports("smda-malpedia", "all_functions.json")