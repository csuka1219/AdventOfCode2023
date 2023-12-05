#!/usr/bin/env python3
import helper
import re


COLORS = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

def is_possible_game(input_string: str) -> bool:
    pattern = re.compile(r'\b(\d+)\s+(\w+)\b')
    matches = pattern.findall(input_string)

    for match in matches:
        count, color = match
        count = int(count)
        possible = not COLORS[color] < count
        if possible == False:
            return False
    
    return True


def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")
    result = 0

    for idx, line in enumerate(lines):
        if is_possible_game(line):
            result += idx + 1
    
    print(result)



##################################################

if __name__ == "__main__":
    main()