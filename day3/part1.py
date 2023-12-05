#!/usr/bin/env python3
import re
import helper

class Number:
  def __init__(self, y, start, end, value):
    self.y = y
    self.start = start
    self.end = end
    self.value = value

class Special:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def get_adjacent_positions(self, matrix):
        adjacent_positions = []

        def is_valid_position(r, c):
            return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])

        for r_offset in [-1, 0, 1]:
            for c_offset in [-1, 0, 1]:
                if r_offset == 0 and c_offset == 0:
                    continue  # Skip the current position
                new_row, new_col = self.y + r_offset, self.x + c_offset
                if is_valid_position(new_row, new_col):
                    adjacent_positions.append((new_row, new_col))

        return adjacent_positions
    
    

def get_numbers(input_string: str, index: int) -> list[Number]:
    matches = re.finditer(r'\d+', input_string)
    lst = []
    for match in matches:
        lst.append(Number(index, match.start(), match.end(), int(input_string[match.start(): match.end()])))
    
    return lst

def get_specials(input_string: str, index: int) -> list[Number]:
    matches = re.finditer(r'[^a-zA-Z0-9\s.]', input_string)
    lst = []
    for match in matches:
        lst.append(Special(index, match.start()))
    
    return lst

def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")
    numbers = []
    specials = []
    result = 0
    for idx, line in enumerate(lines):
       numbers.extend(get_numbers(line, idx))
       specials.extend(get_specials(line, idx))
       
    for special_char in specials:
        adjacent_positions = special_char.get_adjacent_positions(lines)
        
        for number in numbers:
            for i in range(number.start, number.end):
                position = (number.y, i)
                if position in adjacent_positions:
                    result += number.value
                    break
    print(result)


##################################################

if __name__ == "__main__":
    main()