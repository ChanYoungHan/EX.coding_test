from pathlib import Path
import re

from input_output.inout_interface import get_inout_string

input_list = [x for x in Path("input_output").glob("input*")]
print(input_list)

from category.solution_interface import solution

patern = re.compile("input*")
for idx, input_file in enumerate(input_list):
    print(f"examle {idx + 1} of total {len(input_list)} \n I/O :  ")
    io = get_inout_string(
        input_file, Path("input_output", patern.sub("output", input_file.name))
    )
    print(io)
    print(solution(io.input))
