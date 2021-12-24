import math
from typing import List, Dict

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


def totient_euler_range(n: int) -> np.ndarray:
    """
    calculate simultaneously the phi() of all numbers from 0 to n-1
    :param n: the highest number to get phi() of
    :return: a list of the results of phi() of all numbers from 0 to n-1
    """
    results = np.array(range(n), dtype="float64")  # init an array
    for p in sympy.primerange(1, n + 1):
        # for each prime, multiply all numbers it divides by the known formula
        results[p::p] *= (1 - 1 / p)
    # return [int(i) for i in results]
    return results.astype("int64")


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def lcm_list(nums: List[int]) -> int:
    """
    calculate the lcm of the input list
    """
    factors: Dict[int, int] = dict()
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
    """
    returns gcd, x, y such that x*a+b*y=gcd
    """
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


def sieve_primes(n) -> np.ndarray:
    flags = np.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, int(math.sqrt(n) + 1)):
        if flags[i]:
            """
            you may think we should start at i instead of i*i and we are skipping nums this way,
            but notice that we are skipping nums like 2i, 3i, ..., ki
            with k<i so that has already been taken care of with k
            """
            flags[i * i::i] = False
    return np.flatnonzero(flags)


def co_primes(a: int, b: int) -> bool:
    return math.gcd(a, b) == 1


def coprime_to_list(num: int, nums_list: List[int]):
    return all(co_primes(num, x) for x in nums_list)


def get_co_primes(n: int) -> np.ndarray:
    """
    :param n: an input number
    :return: a list of all numbers from 1 to n-1 that are co primes with n
    """
    results = np.ones(n, dtype=bool)  # init an array
    results[0] = False
    for p in sympy.primefactors(n):
        # for each prime, set all numbers it divides to false
        results[p::p] = False
    return np.flatnonzero(results)


def sieve_primes_3mod4(n) -> np.ndarray:
    """
    like sieve_prime() but only primes s.t. p%4=3
    """
    flags = np.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, int(math.sqrt(n) + 1)):
        if flags[i]:
            """
            you may think we should start at i instead of i*i and we are skipping nums this way,
            but notice that we are skipping nums like 2i, 3i, ..., ki
            with k<i so that has already been taken care of with k
            """
            flags[i * i::i] = False
    flags[1::4] = False
    flags[2] = False
    return np.flatnonzero(flags)
