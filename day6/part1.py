#!/usr/bin/env python3
import helper
import math

def parse(lines: list[str]) -> list[tuple[int,int]]:
    result = []

    for line1, line2 in zip(lines[0].split(':')[1].split(), lines[1].split(':')[1].split()):
        number1 = int(line1)
        number2 = int(line2)
        result.append((number1, number2))

    return result

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
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")
    time_distance_pairs = parse(lines)
    count_of_wins_list = []

    for time_distance_pair in time_distance_pairs:
        count_of_wins_list.append(process(time_distance_pair))
    
    result = math.prod(count_of_wins_list)
    print(result)

##################################################

if __name__ == "__main__":
    main()