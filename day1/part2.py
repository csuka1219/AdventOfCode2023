#!/usr/bin/env python3
import re
import helper

DIGITS = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    
def text2number(text: str) -> int:
    if text.isdigit():
        return int(text)
    # else
    return DIGITS[text]

def find_first_last_digits(input_string: str) -> tuple[int, int]:
    digit_pattern = re.compile(r'(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine))')

    digits = [match.group(1) for match in digit_pattern.finditer(input_string)]
    first_digit = digits[0] if digits else None
    last_digit = digits[-1] if digits else None

    return first_digit, last_digit

def numcat(first: int, last: int) -> int:
    return first * 10 + last

def main() -> None:
    #lines = read_lines("example2.txt")
    lines = helper.read_lines("input.txt")
    result = 0
    for item in lines:
        first, last =  find_first_last_digits(item)
        first, last = (DIGITS[first], DIGITS[last])
        result += numcat(first, last)
    print(result)

##############################################################################

if __name__ == "__main__":
    main()