#!/usr/bin/env python3
import helper

def proccess(input_string: str) -> int:
    numbers = input_string.split(':')[1].split('|')
    winning_numbers = set(numbers[0].split())
    numbers_you_have = set(numbers[1].split())
    matched_count = len(winning_numbers.intersection(numbers_you_have))
    if matched_count > 0:
        return 2 ** (matched_count-1)
    else:
        return 0

def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")
    result = 0
    for line in lines:
        result += proccess(line)
    print(result)

##################################################

if __name__ == "__main__":
    main()