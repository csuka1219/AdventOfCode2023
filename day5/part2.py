#!/usr/bin/env python3
import re
import helper
import sys

class NumberExtractor:
    def __init__(self, input_string):
        self.input_string = input_string
        self.numbers_by_section = self.extract_numbers_by_section()
        self.seeds = self.get_seeds_interval()

    def extract_numbers_by_section(self):
        sections = re.findall(r'(\b(?:\d+\s*)+\b)', self.input_string)
        numbers_by_section = [[int(num) for num in re.findall(r'\b\d+\b', section)] for section in sections]
        return numbers_by_section
    
    def get_seeds_interval(self):
        seed_list = self.numbers_by_section[0]
        return [(seed_list[i], seed_list[i] + seed_list[i + 1] - 1) for i in range(0, len(seed_list), 2)]
    
    def get_location(self, seed: int) -> int:
        pass
    
    def get_destinations(self):
        result = []
        for section in self.numbers_by_section[1::]:
            tmp = []
            for i in range(0, len(section), 3):
                tmp.append((section[i+1],(section[i+1]+section[i+2]-1), (section[i]-section[i+1])))
            result.append(tmp)
        return result

def get_lowest_location(locations):
    lowest = locations[0][0]
    for location in locations:
        lowest = min(location[0], lowest)
    return lowest

def process(seeds, maps):
    lowest = sys.maxsize
    for seed in seeds:
        destinations = []
        destinations.append(seed)
        for map in maps:
            stack = destinations
            destinations = []
            while len(stack) > 0:
                source = stack.pop()
                source_start, source_end = source
                for item in map:
                    map_start, map_end, adjust = item
                    if source_start >= map_start and source_end <= map_end:
                        destinations.append((source_start+adjust, source_end+adjust))
                        break
                    if source_end < map_start or source_start > map_end:
                        continue
                    if source_start < map_start:
                        stack.append((source_start, map_start-1))
                        stack.append((map_start, source_end))
                        break
                    if source_end > map_end:
                        stack.append((source_start, map_end))
                        stack.append((map_end+1, source_end))
                        break
                else:
                    destinations.append(source)
        seed_lowest = get_lowest_location(destinations)
        lowest = min(lowest, seed_lowest)
    return lowest

def main() -> None:
    #input_string = helper.read("example.txt")
    input_string = helper.read("input.txt")
    number_extractor = NumberExtractor(input_string)
    maps = number_extractor.get_destinations()
    lowest = process(number_extractor.get_seeds_interval(), maps)
    
    print(lowest)

##################################################
if __name__ == "__main__":
    main()