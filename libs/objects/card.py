from __future__ import annotations

from collections import Counter
from typing import List, Dict, Union


class Card:
    def __init__(self, number: Union[str, int], shape: str):
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
        return f"{self.number},{self.shape}"

    @staticmethod
    def sort_by_number(cards: List[Card]) -> List[Card]:
        """
        :param cards: cards list
        :return: the input list of cards sorted by number
        """
        return sorted(cards, key=lambda c: c.number)

    @staticmethod
    def shapes_count(cards: List[Card]) -> Dict[str, int]:
        """
        :param cards: cards list
        :return: dict of counts for each shape
        """
        return Counter([c.shape for c in cards])

    @staticmethod
    def numbers_count(cards: List[Card]) -> Dict[int, int]:
        """
        :param cards: cards list
        :return: dict of counts for each number
        """
        return Counter([c.number for c in cards])
