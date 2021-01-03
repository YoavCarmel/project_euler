from sympy import divisors
from itertools import combinations_with_replacement


def ans():
    abundant = []
    n = 28123
    for i in range(1, n + 1):
        if sum(divisors(i)) - i > i:
            abundant.append(i)
    expressed = set()
    for i, j in combinations_with_replacement(abundant, 2):
        expressed.add(i + j)
    return sum(set([i for i in range(n + 1)]).difference(expressed))
