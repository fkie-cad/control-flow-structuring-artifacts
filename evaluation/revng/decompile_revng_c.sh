#!/bin/bash

# Get the binary file path and output file path as arguments
binary_file="$1"
output_file="$2"

# Check if the required arguments are provided
if [ -z "$binary_file" ] || [ -z "$output_file" ]; then
  echo "Usage: $0 <binary_file> <output_file>"
  exit 1
fi

# Check if the binary file exists
if [ ! -f "$binary_file" ]; then
  echo "Error: Binary file '$binary_file' not found."
  exit 1
fi

# Source the environment file
source ./environment

# Run the revng commands
revng artifact --analyze --progress decompile-to-single-file "$binary_file" | revng ptml > "$output_file"

# Check the exit codes of the commands
if [ $? -ne 0 ]; then
  echo "Error: revng commands failed."
  exit 1
fi

echo "Decompilation complete. Output written to $output_file"