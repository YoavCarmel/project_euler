from itertools import combinations
from typing import List

from sympy import primerange

from libs.numbers_properties import same_digits


def ans():
    # more and small prime factors lead to big ratio. we want max of 2 prime factors
    # for one factor, this is not possible to have the same digits. so only need 2 factors
    ten_power = 7
    limit = 10 ** ten_power
    primes: List[int] = list(primerange(10 ** 3, 10 ** 4))  # no need for 10**7 if we start from 10**3
    result = 0
    calc_result = 1000
    for p1, p2 in combinations(primes, 2):
        p1p2 = p1 * p2
        if p1p2 < limit:
            te = (p1 - 1) * (p2 - 1)
            if p1p2 / te < calc_result and same_digits(p1p2, te):
                result = p1p2
                calc_result = p1p2 / te
    return result
