#!/usr/bin/env python3
import re
import helper
import sys

class NumberExtractor:
    def __init__(self, input_string):
        self.input_string = input_string
        self.numbers_by_section = self.extract_numbers_by_section()
        self.seeds = self.numbers_by_section[0]

    def extract_numbers_by_section(self):
        sections = re.findall(r'(\b(?:\d+\s*)+\b)', self.input_string)
        numbers_by_section = [[int(num) for num in re.findall(r'\b\d+\b', section)] for section in sections]
        return numbers_by_section
    
    def get_location(self, seed: int) -> int:
        result = seed
        for section in self.numbers_by_section[1::]:
            for i in range(0, len(section), 3):
                if section[i+1] <= result <= (section[i+1] + section[i+2]):
                    result = result + (section[i] - section[i+1]) 
                    break
        return result



def main() -> None:
    # input_string = helper.read("example.txt")
    input_string = helper.read("input.txt")
    number_extractor = NumberExtractor(input_string)
    result = sys.maxsize
    for seed in number_extractor.seeds:
        location = number_extractor.get_location(seed)
        result = location if location < result else result

    print(result)

##################################################

if __name__ == "__main__":
    main()