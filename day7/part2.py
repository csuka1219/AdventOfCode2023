#!/usr/bin/env python3
import helper
import collections

CARDS = "J23456789TQKA"

class Game:
    def __init__(self, lines: list[str]) -> None:
        self.hands = []
        self.bids = {}
        self.fill(lines)

    def fill(self, lines: list[str]) -> None:
        for line in lines:
            hand = line.split()[0]
            self.hands.append(hand)
            self.bids[hand] = int(line.split()[1])
    
    def sort(self) -> None:
        def get_number_of_types(hand: str) -> int:
            number_of_J = hand.count('J')
            if number_of_J > 0 and number_of_J < 5:
                most_common_char, number_of_most_common_char = collections.Counter(hand).most_common(1)[0]
                if most_common_char == 'J':
                    number_of_most_common_char += collections.Counter(hand).most_common(2)[1][1]
                else:
                    number_of_most_common_char += number_of_J
                return number_of_most_common_char * 100 // (len(collections.Counter(hand).most_common()) - 1)
            return collections.Counter(hand).most_common(1)[0][1] * 100 // len(collections.Counter(hand).most_common())
        
        def get_strength_of_order(hand: str) -> list[int]:
            res = []
            for c in hand:
                res.append(CARDS.find(c))
            return res
        
        self.hands.sort(key=lambda x: (get_number_of_types(x),get_strength_of_order(x)))
    
    def get_result(self) -> int:
        result = 0
        for idx, hand in enumerate(self.hands):
            result += self.bids.get(hand)*(idx+1)
        return result

def main() -> None:
    # lines = helper.read_lines("example.txt")
    lines = helper.read_lines("input.txt")
    game = Game(lines)
    game.sort()
    result = game.get_result()
    print(result)

##################################################

if __name__ == "__main__":
    main()