from typing import List

from sympy import isprime, nextprime

from libs.calculations.numbers_properties import is_square


def ans():
    num: int = 3
    primes: List[int] = list()
    while True:
        if not is_possible(num, primes):
            return num
        num += 2


def is_possible(n: int, primes: List[int]) -> bool:
    """
    :param n: num to check
    :param primes: already found primes
    :return: True if it is possible
    """
    p: int = 3
    if isprime(n):
        return True
    for p in primes:  # already found primes
        # p+2*s*s=n so s*s=(n-p)/2
        if is_square((n - p) / 2):
            return True
    while p < n:  # new primes
        # p+2*s*s=n so s*s=(n-p)/2
        if is_square((n - p) / 2):
            return True
        p = nextprime(p)
        primes.append(p)
    return False
