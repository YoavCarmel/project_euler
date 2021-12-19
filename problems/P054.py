from typing import TextIO, List

from objects.card import Card


def ans():
    count: int = 0
    f: TextIO = open("files//P054.txt")
    for line in f.readlines():
        line_split: List[str] = line.strip("\n").split(" ")
        # get players
        p1: List[Card] = convert_list_to_cards(line_split[:5])
        p2: List[Card] = convert_list_to_cards(line_split[5:])
        # get players powers
        power_p1: int = power(p1)
        power_p2: int = power(p2)
        if power_p1 > power_p2:
            # player 1 has the stronger hand
            count += 1
        elif power_p1 == power_p2 and tie_breaker(p1, p2) == 1:
            # players have the same power but player 1 has the stronger hand by a tie breaker
            count += 1
    return count


def convert_list_to_cards(p: List[str]) -> List[Card]:
    """
    :param p: a list of strings
    :return: a list of cards
    """
    return [Card(p[i][0], p[i][1]) for i in range(5)]


def power(input_cards: List[Card]) -> int:
    """
    :param input_cards: a hand of 5 cards
    :return: the power of the hand
    """

    def straight_flush(cards) -> bool:
        return flush(cards) and straight(cards)

    def four_of_a_kind(cards) -> bool:
        return max(Card.numbers_count(cards).values()) == 4

    def full_house(cards) -> bool:
        n = Card.numbers_count(cards)
        if len(n.keys()) == 2:
            values = set(n.values())
            return len(values.difference({2, 3})) == 0

    def flush(cards) -> bool:
        return max(Card.shapes_count(cards).values()) == 5

    def straight(cards) -> bool:
        cards = Card.sort_by_number(cards)
        # need to check 0 - 4, 1 - 5, 2 - 6, ace to 5
        if cards[0].number == 2 and cards[1].number == 3 and cards[2].number == 4 and cards[3].number == 5 and \
                cards[4].number == 14:
            return True
        for j in range(4):  # the 5th is checked by the 4th
            if cards[j + 1].number - cards[j].number != 1:
                return False
        return True

    def three_of_a_kind(cards) -> bool:
        return max(Card.numbers_count(cards).values()) == 3

    def two_pair(cards) -> bool:
        n = list(Card.numbers_count(cards).values())
        return n == [2, 2, 1] or n == [2, 1, 2] or n == [1, 2, 2]

    def pair(cards) -> bool:
        return max(Card.numbers_count(cards).values()) == 2

    if straight_flush(input_cards):
        return 9
    elif four_of_a_kind(input_cards):
        return 8
    elif full_house(input_cards):
        return 7
    elif flush(input_cards):
        return 6
    elif straight(input_cards):
        return 5
    elif three_of_a_kind(input_cards):
        return 4
    elif two_pair(input_cards):
        return 3
    elif pair(input_cards):
        return 2
    else:
        return 1


def tie_breaker(player1: List[Card], player2: List[Card]) -> int:
    """
    break the tie of the players
    :param player1: first player
    :param player2: second player
    :return: winning player: 1/2, 0 if still tie
    """

    def get_keys_of_value(d, v):  # returns all keys with v values, sorted from biggest to smallest
        keys = list()
        for i in d.keys():
            if d[i] == v:
                keys.append(i)
        return tuple(reversed(sorted(keys)))

    def high_card(p1, p2) -> int:
        p1 = Card.sort_by_number(p1)
        p2 = Card.sort_by_number(p2)
        for i in range(4, 0, -1):
            if p1[i].number > p2[i].number:
                return 1
            elif p1[i].number < p2[i].number:
                return 2
        return 0

    def pair(p1, p2) -> int:
        if get_keys_of_value(Card.numbers_count(p1), 2) > get_keys_of_value(Card.numbers_count(p2), 2):
            return 1
        elif get_keys_of_value(Card.numbers_count(p1), 2) < get_keys_of_value(Card.numbers_count(p2), 2):
            return 2
        # else, pair is tied
        return high_card(p1, p2)

    def two_pair(p1, p2) -> int:
        if get_keys_of_value(Card.numbers_count(p1), 2) > get_keys_of_value(Card.numbers_count(p2), 2):
            return 1
        elif get_keys_of_value(Card.numbers_count(p1), 2) < get_keys_of_value(Card.numbers_count(p2), 2):
            return 2
        # else, tie in both pairs
        return high_card(p1, p2)

    def three_of_a_kind(p1, p2) -> int:
        if get_keys_of_value(Card.numbers_count(p1), 3) > get_keys_of_value(Card.numbers_count(p2), 3):
            return 1
        elif get_keys_of_value(Card.numbers_count(p1), 3) < get_keys_of_value(Card.numbers_count(p2), 3):
            return 2
        # else, three is tied
        return high_card(p1, p2)

    def straight(p1, p2) -> int:
        p1 = Card.sort_by_number(p1)
        p2 = Card.sort_by_number(p2)
        if (p1[0] == 2 and p1[4] == 14) and (p2[0] == 2 and p2[4] == 14):
            return 0
        elif p1[0] == 2 and p1[4] == 14:
            return 2
        elif p2[0] == 2 and p2[4] == 14:
            return 1
        else:
            return high_card(p1, p2)

    def flush(p1, p2) -> int:
        return high_card(p1, p2)

    def full_house(p1, p2) -> int:
        if get_keys_of_value(Card.numbers_count(p1), 3) > get_keys_of_value(Card.numbers_count(p2), 3):
            return 1
        elif get_keys_of_value(Card.numbers_count(p1), 3) < get_keys_of_value(Card.numbers_count(p2), 3):
            return 2
        # else, tie in threes, check pairs
        if get_keys_of_value(Card.numbers_count(p1), 2) > get_keys_of_value(Card.numbers_count(p2), 2):
            return 1
        elif get_keys_of_value(Card.numbers_count(p1), 2) < get_keys_of_value(Card.numbers_count(p2), 2):
            return 2
        # else, complete tie
        return 0

    def four_of_a_kind(p1, p2) -> int:
        if get_keys_of_value(Card.numbers_count(p1), 4) > get_keys_of_value(Card.numbers_count(p2), 4):
            return 1
        elif get_keys_of_value(Card.numbers_count(p1), 4) < get_keys_of_value(Card.numbers_count(p2), 4):
            return 2
        # else, tie in four, check the 5th card
        return high_card(p1, p2)

    def straight_flush(p1, p2) -> int:
        return straight(p1, p2)

    power_value = power(player1)
    if power_value == 1:
        return high_card(player1, player2)
    elif power_value == 2:
        return pair(player1, player2)
    elif power_value == 3:
        return two_pair(player1, player2)
    elif power_value == 4:
        return three_of_a_kind(player1, player2)
    elif power_value == 5:
        return straight(player1, player2)
    elif power_value == 6:
        return flush(player1, player2)
    elif power_value == 7:
        return full_house(player1, player2)
    elif power_value == 8:
        return four_of_a_kind(player1, player2)
    elif power_value == 9:
        return straight_flush(player1, player2)
    else:
        print("something is wring in winner ot 2")
        return -1
