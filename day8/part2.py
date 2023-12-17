#!/usr/bin/env python3
import helper
import re
from itertools import cycle
import math

class Network:
    def __init__(self, lines: list[str]) -> None:
        self.instructions = lines[0]
        self.nodes: dict[str, tuple[str, str]] = {}
        self.fill_nodes(lines[2::])

    def fill_nodes(self, lines: list[str]) -> None:
        for line in lines:
            key, left, right = re.findall("[a-zA-Z]+", line)
            self.nodes[key] = (left, right)

    def get_number_of_steps(self, current_node_key) -> int:
        steps = 0
        for c in cycle(self.instructions):
            if current_node_key.endswith("Z"):
                return steps
            steps += 1
            if c == 'L':
                current_node_key = self.nodes[current_node_key][0]
            else:
                current_node_key = self.nodes[current_node_key][1]


def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")
    network = Network(lines)
    steps = []
    for node_key in network.nodes.keys():
        if node_key.endswith("A"):
            steps.append(network.get_number_of_steps(node_key))
    result = math.lcm(*steps)
    print(result)

##################################################

if __name__ == "__main__":
    main()