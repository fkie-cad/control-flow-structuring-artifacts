#!/bin/bash

# Copy the parser
cp /shared_volume/parse_data_set.py /decompiler/retdec

# Run the selected Python script with any arguments
python3 decompile_retdec.py

# Copy the json files to the output volume
cp /decompiler/retdec/results_retdec.json /shared_volume/retdec/
rm -rf /shared_volume/retdec/decompiler_logdata/
mkdir /shared_volume/retdec/decompiler_logdata/
cp /decompiler/retdec/log_data_*.log /shared_volume/retdec/decompiler_logdata/
rm -rf /shared_volume/retdec/decompiler_output/
mkdir /shared_volume/retdec/decompiler_output/
cp /decompiler/retdec/output_*.c /shared_volume/retdec/decompiler_output/
