#!/bin/bash

# Copy the parser
cp /shared_volume/parse_data_set.py /decompiler/revng

# Run the selected Python script with any arguments
python3 decompile_revng_c.py

# Copy the json files to the output volume
cp /decompiler/revng/results_revngc.json /shared_volume/revngc/
# Remove folder for decompiler output if it exists
rm -rf /shared_volume/revngc/decompiler_output/
mkdir /shared_volume/revngc/decompiler_output/
cp /decompiler/revng/output_*.c /shared_volume/revngc/decompiler_output/
