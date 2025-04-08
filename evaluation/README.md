### General Remarks

For our evaluation, we used the Malpedia dataset.  
To replicate our evaluation, you need a Malpedia account or an alternative malware corpus with representative samples.  
Since Malpedia contains malware samples that are not publicly available, we cannot publish the corresponding hashes.  
However, because we randomly selected samples, similar results can be reproduced by choosing the same number of random samples with the same criteria.

Our evaluation uses two commercial decompilers: Hex-Rays and Binary Ninja.  
Licenses for these decompilers are required to decompile the binaries.  
Additionally, dewolf is built on Binary Ninja's MLIL, so a Binary Ninja license is also necessary for its use.

### Creation data-set

1. Install the requirements: `python -m pip install -r requirements.txt`
2. Disassemble all malpedia samples: `python dissasemble_all_malpedia_samples.py`
   - Generates the directory `smda-malpedia`
3. Collect malpedia data: `python collect_all_malpedia_data.py`
   - Generates the file `all_functions.json`
4. Generate the data-set: `python generate_stratified_dataset.py`
   - Update the mapledia path "MALPEDIA_PATH"
   - Generates the file `stratified_dataset_functions.json`

### Generate Decompiler-Output

For each decompiler, we provide scripts to generate the output.
Each script generates a file `results_{decompiler}.json`, which we then use to extract metrics.

###### SAILR, DREAM, Phoenix
To decompile all samples with `SAILR`, `DREAM`, or `Phoenix`, we used the corresponding implementation integrated into angr.
A Dockerfile is provided to generate the outputs.
Instructions for its use are in the `README.md` in the `angr` folder.
The folder containing all Malpedia samples should be in the `evaluation` folder of the artifacts directory for Docker to access it.

###### Binary Ninja
To decompile all samples with Binary Ninja, you need a Binary Ninja license and must install the Binary Ninja Python API along with the required dependencies.
Update the `MALPEDIA_PATH` in the script and run it to generate the decompilation outputs.

###### dewolf
To use dewolf, install dewolf (which requires a Binary Ninja license) and the additional requirements for the script.
Update the `MALPEDIA_PATH` and `DEWOLF_PATH` in the script, then run it to obtain the decompilation outputs.

###### Ghidra
To decompile all samples with Ghidra, install Ghidra and the required dependencies.
Update the `MALPEDIA_PATH` and `GHIDRA_PATH` in the script, then run it to generate the decompilation outputs.

###### Hex-Rays
To decompile all samples with Hex-Rays, obtain a Hex-Rays license and install the required dependencies.
Update the `MALPEDIA_PATH` and `IDA_PATH` in the `run_ida.py` script, then run it.
Unlike other decompilers, no timeout is used during decompilation, and each output is written to a separate file.
Only functions decompiled within the given time frame are considered.

###### Radare
To decompile all samples with Radare, use the Dockerfile provided in the `radare` folder together with instructions for its use in the `README.md`.
Ensure the folder containing all Malpedia samples is in the `evaluation` folder of the artifacts directory for Docker to access it.

###### RetDec
To decompile all samples with RetDec, use the Dockerfile provided in the `retdec` folder together with instructions for its use in the `README.md`.
Ensure the folder containing all Malpedia samples is in the `evaluation` folder of the artifacts directory for Docker to access it.

###### Revng
To decompile all samples with Revng, use the Dockerfile provided in the `revng` folder together with instructions for its use in the `README.md`.
Ensure the folder containing all Malpedia samples is in the `evaluation` folder of the artifacts directory for Docker to access it.

### Generate Metrics

Install the required dependencies and `astyle` for code formatting to ensure all decompiler outputs are formatted consistently.
Update the path to the results (`PATH_TO_RESULTS`) if needed.
The results are saved for each decompiler in a JSON file: `metrics_{decompiler_name}.json`.
