from typing import Dict

from sympy import divisors


def ans():
    sums: Dict[int, int] = dict()
    n: int = 10000
    # calculate the value of all cells
    for i in range(1, n + 1):
        sums[i] = sum(divisors(i)) - i
    s: int = 0
    # find pairs
    for i in range(1, n + 1):
        if sums[i] in sums and sums[i] != i and sums[sums[i]] == i:
            s += i
    return s
