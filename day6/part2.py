#!/usr/bin/env python3
import helper
import re

def parse(lines: list[str]) -> tuple[int,int]:
    pattern = re.compile(r'\d+')

    matches = pattern.findall(lines)

    matches_length = len(matches)//2

    time_number = int(''.join(matches[:matches_length]))
    distance_number = int(''.join(matches[matches_length:]))
    return (time_number, distance_number)

def process(time_distance_pair: tuple[int, int]) -> int:
    time, distance = time_distance_pair
    first, last = 0, 0
    first_win = distance//time + 1
    for used_time in range(first_win, time):
        remaining_time = time-used_time
        traveled_distance = remaining_time*used_time
        if traveled_distance > distance:
            first = used_time
            break

    # I use two loops for less iterations 
    for used_time in range(time, first_win, -1):
        remaining_time = time-used_time
        traveled_distance = remaining_time*used_time
        if traveled_distance > distance:
            last = used_time
            break

    return last - first + 1

def main() -> None:
    # lines = helper.read("example.txt")
    lines = helper.read("input.txt")
    time_distance_pair = parse(lines)
    result = process(time_distance_pair)
    print(result)

##################################################

if __name__ == "__main__":
    main()