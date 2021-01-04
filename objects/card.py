from __future__ import annotations

from collections import defaultdict
from typing import List, Dict, Union


class Card:
    def __init__(self, number: Union[str,int], shape: str):
        # 2-15 as two-ten,jack,queen,king,ace,joker
        if number == "T":
            self.number = 10
        elif number == "J":
            self.number = 11
        elif number == "Q":
            self.number = 12
        elif number == "K":
            self.number = 13
        elif number == "A":
            self.number = 14
        else:
            self.number = int(number)
        # 1-4 as clubs,diamonds,hearts,spades
        self.shape = shape

    def __str__(self):
        return str(self.number) + "," + self.shape

    @staticmethod
    def sort_by_number(cards: List[Card]) -> List[Card]:
        """
        :param cards: cards list
        :return: the input list of cards sorted by number
        """
        return list(sorted(cards, key=lambda c: c.number))

    @staticmethod
    def shapes_count(cards: List[Card]) -> Dict[str, int]:
        """
        :param cards: cards list
        :return: dict of counts for each shape
        """
        shapes: Dict[str, int] = defaultdict(int)
        for c in cards:
            shapes[c.shape] += 1
        return shapes

    @staticmethod
    def numbers_count(cards: List[Card]) -> Dict[int, int]:
        """
        :param cards: cards list
        :return: dict of counts for each number
        """
        numbers: Dict[int, int] = defaultdict(int)
        for c in cards:
            numbers[c.number] += 1
        return numbers
