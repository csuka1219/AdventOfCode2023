#!/usr/bin/env python3

def read_lines(fname: str) -> list[str]:
    with open(fname) as f:
        return f.read().strip().splitlines()
    
def get_first_and_last_digits(input_string) -> None:
    digits = [int(char) for char in input_string if char.isdigit()]

    if digits:
        return digits[0], digits[-1]
    else:
        return None, None

def numcat(first, last) -> int:
    return first * 10 + last


def main() -> None:
    #lines = read_lines("example.txt")
    lines = read_lines("input.txt")
    result = 0
    for item in lines:
        first,last = get_first_and_last_digits(item)
        if first is None or last is None: continue
        result += numcat(first, last)
    print(result)

##############################################################################

if __name__ == "__main__":
    main()