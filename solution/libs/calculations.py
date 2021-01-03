import math
from typing import List, Iterable

import numpy as np
import sympy
from itertools import chain, combinations


# from scipy.special import binom

def multinom(params):
    if len(params) == 1:
        return 1
    return binom(sum(params), params[-1]) * multinom(params[:-1])


def binom(n: int, k: int) -> int:
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def base2(x: int) -> int:
    return int(bin(x)[2:])


def totient_euler(n: int) -> int:
    result = float(n)
    for i in sympy.primefactors(n):
        result *= (1 - 1 / i)
    return int(result)


def totient_euler_range(n: int) -> List[int]:
    l = np.array(range(n), dtype='float64')
    for p in sympy.primerange(1, n + 1):
        l[p::p] *= (1 - 1 / p)
    return [int(i) for i in l]


def smallest_number_with_digit_sum(n: int) -> int:
    return int(str(n % 9) + "9" * (n // 9))


def powerset(iterable: Iterable, with_empty=True, as_iterable=False):
    s = list(iterable)
    res = chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
    if not with_empty:
        next(res,None)
    if as_iterable:
        return res
    return list(res)
