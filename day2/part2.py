#!/usr/bin/env python3
import helper
import re

def multiply_dict_values(input_dict: dict[str,int]) -> int:
    result = 1
    for value in input_dict.values():
        result *= value
    return result

def get_maximum_colors_dict(input_string: str) -> dict[str,int]:
    pattern = re.compile(r'\b(\d+)\s+(\w+)\b')
    matches = pattern.findall(input_string)

    color_counts = {
        "red" : 0,
        "green" : 0,
        "blue" : 0
    }

    for match in matches:
        count, color = match
        count = int(count)
        if color_counts[color] < count:
            color_counts[color] = count
    
    return color_counts


def main() -> None:
    # lines = helper.read_lines("example2.txt")
    lines = helper.read_lines("input.txt")
    result = 0

    for line in lines:
        maximum_colors = get_maximum_colors_dict(line)
        result += multiply_dict_values(maximum_colors)
    
    print(result)



##################################################

if __name__ == "__main__":
    main()