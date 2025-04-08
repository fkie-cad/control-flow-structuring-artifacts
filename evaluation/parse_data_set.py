import json
from dataclasses import dataclass
from pathlib import Path

from tqdm import tqdm

DATA_PATH = Path("/shared_volume")
DATA_FILE = Path("dataset/stratified_dataset_functions.json")


@dataclass
class Function:
    binary_sha: str
    packed_sha: str
    path: Path
    address: int
    basic_block_number: int


def parse_data():
    try:
        with open(DATA_PATH / DATA_FILE, "r") as json_data:
            try:
                function_list = json.load(json_data)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON file: {e}")
    except FileNotFoundError:
        raise FileNotFoundError(f"Error: File '{DATA_PATH}' not found.")

    for function in tqdm(function_list):
        try:
            function_instance = Function(
                binary_sha=function.get("binary_sha256", ""),  # Use .get() with default
                packed_sha=function.get("packed_sha256", ""),
                path=DATA_PATH / "malpedia" / function.get("malpedia_path", ""),
                address=int(function.get("function_address", ""), 16),
                basic_block_number=int(function.get("num_blocks", 0)),
            )
            yield function_instance

        except KeyError as e:  # Catch if a key is missing
            print(f"Error: Missing key {e} on function: {function}")
