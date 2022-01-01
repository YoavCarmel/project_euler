from math import sqrt
from typing import List, Set

from libs.calculations.palindromes import is_palindrome


def ans():
    n = 10 ** 8
    squares: List[int] = [0]
    res: Set[int] = set()
    # create array of sums of squares
    for i in range(1, int(sqrt(n)) + 1):
        squares.append(i ** 2 + squares[-1])
    # go over of subsequences and check if palindromes
    for i in range(len(squares)):
        # go over all bigger numbers, and break when reaching a difference to big
        for j in range(i + 2, len(squares)):
            x = squares[j] - squares[i]
            if x > n:
                break
            if is_palindrome(x):
                res.add(x)
    return sum(res)
