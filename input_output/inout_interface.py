from pathlib import Path
from munch import munchify


def get_inout_string(input: Path, output: Path):
    temp_dict = munchify(
        {
            "input": "",
            "output": "",
        }
    )
    with open(input, "r") as f:
        temp_dict.input = f.read()
    with open(output, "r") as f:
        temp_dict.output = f.read()
    return temp_dict
