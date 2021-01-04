from libs.types_converting import list_to_num
from sympy import isprime

from itertools import permutations


def ans():
    # notice: every 9 digit and 8 digit pandigital number is divisible by 3, thus not prime
    # generate all 7-digits pandigital and check for primes
    m: int = 0
    for p in permutations(range(1, 7 + 1)):
        num: int = list_to_num(p)
        if isprime(num):
            m = max(m, num)
    return m
