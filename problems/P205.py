from itertools import product
from collections import defaultdict


def ans():
    peter = defaultdict(int)
    for p in product(range(1, 4 + 1), repeat=9):
        peter[sum(p)] += 1
    colin = defaultdict(int)
    for p in product(range(1, 6 + 1), repeat=6):
        colin[sum(p)] += 1

    peter_wins = 0
    for p in peter:
        for c in colin:
            if p > c:
                peter_wins += peter[p] * colin[c]
    return round(peter_wins / (4 ** 9 * 6 ** 6), 7)
