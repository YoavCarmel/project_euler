import math
from typing import List

import numpy as np
import sympy
from sympy import factorint


def totient_euler(n: int) -> int:
    """
    calculate the euler's totient function (phi)
    :param n: the input number of phi
    :return: the result of phi(n)
    """
    # apply exactly the known formula from number theory
    result = float(n)
    for i in sympy.primefactors(n):
        result *= (1 - 1 / i)
    return int(result)


def totient_euler_range(n: int) -> List[int]:
    """
    calculate simultaneously the phi() of all numbers from 0 to n-1
    :param n: the highest number to get phi() of
    :return: a list of the results of phi() of all numbers from 0 to n-1
    """
    results = np.array(range(n), dtype='float64')  # init an array
    for p in sympy.primerange(1, n + 1):
        # for each prime, multiply all numbers it divides by the known formula
        results[p::p] *= (1 - 1 / p)
    return [int(i) for i in results]


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_list(nums: List[int]) -> int:
    factors = dict()
    for i in nums:
        i_factors = factorint(i)
        for k in i_factors:
            if k in factors:
                factors[k] = max(factors[k], i_factors[k])
            else:
                factors[k] = i_factors[k]
    p = 1
    for k in factors:
        p *= (k ** factors[k])
    return p


def gcd_extended_euclid(a, b):
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcd_extended_euclid(b % a, a)

    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def inverse_mod(x: int, n: int):
    """
    :param x: num to find inverse of
    :param n: the Z_n
    :return: y s.t. x*y=gcd(x,n) mod n
    """
    return pow(x, -1, n)


def sieve_primes(n):
    flags = np.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, int(math.sqrt(n) + 1)):
        if flags[i]:
            flags[i * i::i] = False
    return list(np.flatnonzero(flags))


def co_primes(a: int, b: int) -> bool:
    return math.gcd(a, b) == 1


def coprime_to_list(num: int, nums_list: List[int]):
    return co_primes(num, lcm_list(nums_list))


def get_co_primes(n: int) -> List[int]:
    """
    :param n: an input number
    :return: a list of all numbers from 1 to n-1 that are co primes with n
    """
    results = np.array(range(n), dtype='bool')  # init an array
    for p in sympy.primefactors(n):
        # for each prime, set all numbers it divides to false
        results[p::p] = False
    return [i for i, is_co_prime in enumerate(results) if is_co_prime]