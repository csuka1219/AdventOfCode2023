#!/usr/bin/env python3
import helper

def process(numbers_of_line: [int]) -> int:
    start_idx = 0
    end_idx = len(numbers_of_line) - 1
    result_lst = []

    while True:
        if start_idx == end_idx:
            result_lst.append(numbers_of_line[end_idx])
            start_idx = 0
            end_idx -= 1

        numbers_of_line[start_idx] = numbers_of_line[start_idx + 1] - numbers_of_line[start_idx]

        if all(n == 0 for n in numbers_of_line[0:end_idx]):
            result_lst.append(numbers_of_line[end_idx])
            break

        start_idx += 1

    return sum(result_lst)



def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")

    result = 0
    for line in lines:
        result += process([int(num) for num in line.split()])
    print(result)


##################################################

if __name__ == "__main__":
    main()