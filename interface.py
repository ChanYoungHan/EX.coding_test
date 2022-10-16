from pathlib import Path
import re

from input_output.inout_interface import get_inout_string
from category.greedy.pro2864 import solution

input_list = [x for x in Path("input_output").glob("input*")]
print(input_list)

patern = re.compile("input*")
for idx, input_file in enumerate(input_list):
    io = get_inout_string(
        input_file, Path("input_output", patern.sub("output", input_file.name))
    )
    print(f"examle {idx + 1} of total {len(input_list)} \n I/O : {io}")
    output = solution(io.input)
    if io.output == output:
        mark = "Success"
    else:
        mark = "Fail"
    print(f" [{mark}] output : {output}")
