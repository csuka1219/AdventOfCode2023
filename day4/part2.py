#!/usr/bin/env python3
import helper

scratchcard_dict={

}

def proccess(input_string: str, index: int) -> int:
    numbers = input_string.split(':')[1].split('|')
    winning_numbers = set(numbers[0].split())
    numbers_you_have = set(numbers[1].split())

    matched_count = len(winning_numbers.intersection(numbers_you_have))
    scratchcard_dict[index] = scratchcard_dict.get(index, 0) + 1

    for i in range(index + 1, (index + matched_count + 1)):
        scratchcard_dict[i] = scratchcard_dict.get(i, 0) + scratchcard_dict.get(index, 1)
    return scratchcard_dict[index]

def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")
    result = 0
    for idx, line in enumerate(lines):
        result += proccess(line, idx)
    print(result)

##################################################

if __name__ == "__main__":
    main()