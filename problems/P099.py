from math import log2
from typing import List


def ans():
    numbers: List[List[int]] = load_powers()
    powers: List[float] = []
    for pair in numbers:
        powers.append(pair[1] * log2(pair[0]))
    return powers.index(max(powers)) + 1


def load_powers() -> List[List[int]]:
    """
    :return: a list of pairs, each sublist is just a pair of numbers
    """
    f = open("files//P099.txt")
    numbers: List[List[int]] = []
    for line in f.readlines():
        numbers.append([int(i) for i in line.strip("\n").split(",")])
    return numbers
