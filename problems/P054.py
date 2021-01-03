"""
warning: i just copied my poker game code, so this file is a mess
"""


def ans():
    count = 0
    f = open("files//P054.txt")
    for line in f.readlines():
        line = line.strip("\n").split(" ")
        p1 = line[:5]
        p2 = line[5:]
        convert_list_to_cards(p1)
        convert_list_to_cards(p2)
        if power(p1) > power(p2):
            count += 1
        elif power(p1) == power(p2) and tie_breaker(p1, p2) == 1:
            count += 1
    return count


def convert_list_to_cards(p):
    for i in range(5):
        p[i] = Card(p[i][0], p[i][1])


def print_cards(c):
    s = ""
    for i in c:
        s += str(i) + " "
    return s


###########################################################

class Card:
    def __init__(self, number, shape):
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


###########################################################


def sort_by_number(cards_original):
    cards = cards_original.copy()
    numbers = []
    for c in cards:
        numbers.append(c.number)
    numbers.sort()
    sorted_cards = []
    for i in numbers:
        for c in cards:
            if i == c.number:
                sorted_cards.append(c)
                cards.remove(c)
                break
    return sorted_cards


def shapes_count(cards):
    shapes = dict()
    for c in cards:
        if c.shape not in shapes.keys():
            shapes[c.shape] = 1
        else:
            shapes[c.shape] += 1
    return shapes


def numbers_count(cards):
    numbers = dict()
    for c in cards:
        if c.number not in numbers.keys():
            numbers[c.number] = 1
        else:
            numbers[c.number] += 1
    return numbers


###############################################################

def power(input_cards):
    def straight_flush(cards):
        return flush(cards) and straight(cards)

    def four_of_a_kind(cards):
        return max(numbers_count(cards).values()) == 4

    def full_house(cards):
        n = numbers_count(cards)
        if len(n.keys()) == 2:
            values = set(n.values())
            return len(values.difference({2, 3})) == 0

    def flush(cards):
        return max(shapes_count(cards).values()) == 5

    def straight(cards):
        cards = sort_by_number(cards)
        # need to check 0 - 4, 1 - 5, 2 - 6, ace to 5
        if cards[0].number == 2 and cards[1].number == 3 and cards[2].number == 4 and cards[3].number == 5 and \
                cards[4].number == 14:
            return True
        for j in range(4):  # the 5th is checked by the 4th
            if cards[j + 1].number - cards[j].number != 1:
                return False
        return True

    def three_of_a_kind(cards):
        return max(numbers_count(cards).values()) == 3

    def two_pair(cards):
        n = list(numbers_count(cards).values())
        return n == [2, 2, 1] or n == [2, 1, 2] or n == [1, 2, 2]

    def pair(cards):
        return max(numbers_count(cards).values()) == 2

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


def tie_breaker(player1, player2):
    def get_keys_of_value(d, v):  # returns all keys with v values, sorted from biggest to smallest
        keys = list()
        for i in d.keys():
            if d[i] == v:
                keys.append(i)
        return tuple(reversed(sorted(keys)))

    def high_card(p1, p2):
        p1 = sort_by_number(p1)
        p2 = sort_by_number(p2)
        for i in range(4, 0, -1):
            if p1[i].number > p2[i].number:
                return 1
            elif p1[i].number < p2[i].number:
                return 2
        return 0

    def pair(p1, p2):
        if get_keys_of_value(numbers_count(p1), 2) > get_keys_of_value(numbers_count(p2), 2):
            return 1
        elif get_keys_of_value(numbers_count(p1), 2) < get_keys_of_value(numbers_count(p2), 2):
            return 2
        # else, pair is tied
        return high_card(p1, p2)

    def two_pair(p1, p2):
        if get_keys_of_value(numbers_count(p1), 2) > get_keys_of_value(numbers_count(p2), 2):
            return 1
        elif get_keys_of_value(numbers_count(p1), 2) < get_keys_of_value(numbers_count(p2), 2):
            return 2
        # else, tie in both pairs
        return high_card(p1, p2)

    def three_of_a_kind(p1, p2):
        if get_keys_of_value(numbers_count(p1), 3) > get_keys_of_value(numbers_count(p2), 3):
            return 1
        elif get_keys_of_value(numbers_count(p1), 3) < get_keys_of_value(numbers_count(p2), 3):
            return 2
        # else, three is tied
        return high_card(p1, p2)

    def straight(p1, p2):
        p1 = sort_by_number(p1)
        p2 = sort_by_number(p2)
        if (p1[0] == 2 and p1[4] == 14) and (p2[0] == 2 and p2[4] == 14):
            return 0
        elif p1[0] == 2 and p1[4] == 14:
            return 2
        elif p2[0] == 2 and p2[4] == 14:
            return 1
        else:
            return high_card(p1, p2)

    def flush(p1, p2):
        return high_card(p1, p2)

    def full_house(p1, p2):
        if get_keys_of_value(numbers_count(p1), 3) > get_keys_of_value(numbers_count(p2), 3):
            return 1
        elif get_keys_of_value(numbers_count(p1), 3) < get_keys_of_value(numbers_count(p2), 3):
            return 2
        # else, tie in threes, check pairs
        if get_keys_of_value(numbers_count(p1), 2) > get_keys_of_value(numbers_count(p2), 2):
            return 1
        elif get_keys_of_value(numbers_count(p1), 2) < get_keys_of_value(numbers_count(p2), 2):
            return 2
        # else, complete tie
        return 0

    def four_of_a_kind(p1, p2):
        if get_keys_of_value(numbers_count(p1), 4) > get_keys_of_value(numbers_count(p2), 4):
            return 1
        elif get_keys_of_value(numbers_count(p1), 4) < get_keys_of_value(numbers_count(p2), 4):
            return 2
        # else, tie in four, check the 5th card
        return high_card(p1, p2)

    def straight_flush(p1, p2):
        straight(p1, p2)

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
