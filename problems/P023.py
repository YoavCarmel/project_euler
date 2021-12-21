from itertools import combinations_with_replacement
from typing import List, Set

from sympy import divisors


def ans():
    abundant: List[int] = []
    n: int = 28123
    # add all abundant numbers
    for i in range(1, n + 1):
        if sum(divisors(i)) - i > i:
            abundant.append(i)
    # create all numbers that can be represented by a sum of two abundant numbers
    expressed: Set[int] = set()
    for i, j in combinations_with_replacement(abundant, 2):
        expressed.add(i + j)
    # return sum of all numbers from 1 to n that are not in expressed
    return sum(set([i for i in range(n + 1)]).difference(expressed))
