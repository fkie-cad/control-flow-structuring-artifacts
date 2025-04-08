import hashlib
import json
import os
import random
import re

import matplotlib.pyplot as plt
import numpy as np

MALPEDIA_PATH = "../../../malpedia"

FILE_PATTERN = re.compile(r'^([a-fA-F0-9]{64})_unpacked$')

def calculate_sha256(file_path):
    """Calculate SHA256 hash of a file"""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

# Global cache for filename -> path mapping
filename_to_path = {}

def build_filepath_cache(base_dir=MALPEDIA_PATH):
    """Build cache of filename to filepath mappings"""
    global filename_to_path
    for root, _, files in os.walk(base_dir):
        for filename in files:
            filename_to_path[filename] = os.path.join(root, filename)

def get_filepath(filename):
    """Get filepath from cache"""
    global filename_to_path
    return filename_to_path.get(filename)

# Initialize cache
build_filepath_cache()

# Replace existing filter_functions to use cache
def filter_functions(functions, min_blocks=4):
    """Filter functions by their basic block count"""
    for f in functions:
        if f[2] < min_blocks: continue
        if not FILE_PATTERN.match(f[0]): continue
        filepath = get_filepath(f[0])
        if not filepath: continue
        yield f

def create_stratified_sample(input_file, num_groups, min_blocks=4):
    # Load and filter functions
    with open(input_file, 'r') as f:
        all_functions = json.load(f)
    
    filtered_functions = list(filter_functions(all_functions, min_blocks))

    sampled_functions = random.sample(filtered_functions, num_groups)
    
    return filtered_functions, sampled_functions

def plot_distributions(all_functions, sampled_functions, output_file="distribution.pdf"):
    # Extract basic block counts
    all_blocks = [f[2] for f in all_functions]
    sampled_blocks = [f[2] for f in sampled_functions]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Calculate percentages for all functions
    unique_all, counts_all = np.unique(all_blocks, return_counts=True)
    percentages_all = counts_all / len(all_blocks) * 100
    
    # Calculate percentages for sampled functions
    unique_sampled, counts_sampled = np.unique(sampled_blocks, return_counts=True)
    percentages_sampled = counts_sampled / len(sampled_blocks) * 100
    
    # Plot both distributions
    ax.plot(unique_all, percentages_all, 'b-', label='All Functions', alpha=0.7)
    ax.plot(unique_sampled, percentages_sampled, 'r-', label='Sampled Functions', alpha=0.7)
    
    # Set scales and labels
    ax.set_xscale('log')
    ax.set_xlabel('Number of Basic Blocks')
    ax.set_ylabel('Percentage of Functions')
    ax.set_title('Distribution of Basic Block Counts')
    ax.grid(True, alpha=0.3)
    ax.legend()
    
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()


def save_samples_functions(output_file, sampled_functions):
    with open(output_file, 'w') as f:
        output = list()
        for samplename, address, num_blocks in sampled_functions:
            filepath = get_filepath(samplename)
            output.append({
                "binary_sha256": calculate_sha256(filepath),
                "packed_sha256": FILE_PATTERN.match(samplename).group(1),
                "malpedia_path": os.path.relpath(filepath, MALPEDIA_PATH),
                "function_address": address,
                "num_blocks": num_blocks
            })
        json.dump(output, f, indent=2)

def generate_data_for_tikz_plot(all_functions, sampled_functions, output_file):
    # Extract basic block counts
    all_blocks = [f[2] for f in all_functions]
    sampled_blocks = [f[2] for f in sampled_functions]

    # Calculate percentages for all functions
    unique_all, counts_all = np.unique(all_blocks, return_counts=True)
    percentages_all = counts_all / len(all_blocks) * 100
    
    # Calculate percentages for sampled functions
    unique_sampled, counts_sampled = np.unique(sampled_blocks, return_counts=True)
    percentages_sampled = counts_sampled / len(sampled_blocks) * 100

    with open(f"{output_file}_all.txt", 'w') as f:
        print("BasicBlocks AllFunctions", file=f)
        for bb, perc in zip(unique_all, percentages_all):
            f.write(f"{bb} {perc}\n")

    with open(f"{output_file}_sampled.txt", 'w') as f:
        print("BasicBlocks SampledFunctions", file=f)
        for bb, perc in zip(unique_sampled, percentages_sampled):
            f.write(f"{bb} {perc}\n")

if __name__ == "__main__":
    all_functions, sampled_functions = create_stratified_sample(
        "all_functions.json", 
        num_groups=1000,
        min_blocks=2
    )
    save_samples_functions("stratified_dataset_functions.json", sampled_functions)
    plot_distributions(all_functions, sampled_functions, "stratified_dataset_functions.pdf")
    generate_data_for_tikz_plot(all_functions, sampled_functions, "function_bb_distribution")