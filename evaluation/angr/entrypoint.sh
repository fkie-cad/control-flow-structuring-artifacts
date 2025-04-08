#!/bin/bash

# Get the script name from the environment variable (default to decompile_sailr.py)
script_name="${SCRIPT_NAME:-decompile_sailr.py}"

# Copy the parser & script
cp /shared_volume/parse_data_set.py /decompiler/
cp /shared_volume/angr/"$script_name" /decompiler/

# Construct the full path to the script in the container
script_path="$script_name"

# Check if the script exists
if [ ! -f "$script_path" ]; then
  echo "Error: Script '$script_path' not found. Make sure it exists in the shared volume."
  exit 1
fi

# Run the selected Python script with any arguments
/venv/bin/python3 "$script_path"

# Copy the json files to the output volume
cp /decompiler/results_*.json /shared_volume/angr/
cp /decompiler/angr.log /shared_volume/angr/"${script_name%.*}.log"