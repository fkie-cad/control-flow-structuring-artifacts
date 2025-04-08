#!/bin/bash

# Copy the parser
cp /shared_volume/parse_data_set.py /decompiler/radare2

# Run the selected Python script with any arguments
source .venv/bin/activate
python3 decompile_radare.py

# Copy the json files to the output volume
cp /decompiler/radare2/results_radare.json /shared_volume/radare/
rm -rf /shared_volume/radare/decompiler_logdata/
mkdir /shared_volume/radare/decompiler_logdata/
cp /decompiler/radare2/log_data_*.log /shared_volume/radare/decompiler_logdata/
