import math
from typing import List, Iterable, Set

import numpy as np
import sympy
from itertools import chain, combinations

from objects.frac import Frac
from objects.frac_with_sqrt import QPair, FracWithSqrt


def multinom(params):
    """
    calculate the multinom of the input numbers, the numerator is their sum
    :param params: the numbers to calculate the multinom of
    :return: their multinom
    """
    if len(params) == 1:
        return 1
    # call recursively
    return binom(sum(params), params[-1]) * multinom(params[:-1])


def binom(n: int, k: int) -> int:
    """
    calculate n choose k
    :param n: the top
    :param k: the bottom
    :return: n choose k
    """
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def base2(x: int) -> int:
    """
    :param x: an integer
    :return: the input number in base 2, as int
    """
    return int(bin(x)[2:])


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


def smallest_number_with_digit_sum(n: int) -> int:
    """
    :param n: wanted digits sum
    :return: smallest number with input digits sum
    """
    return int(str(n % 9) + "9" * (n // 9))


def power_set(iterable: Iterable, with_empty: bool = True, as_iterable: bool = False) -> Iterable:
    """
    returns the power set of the input iterable
    :param iterable: the iterable to create its power set
    :param with_empty: include/exclude the empty set
    :param as_iterable: return as iterable or as list
    :return: the power set
    """
    s = list(iterable)
    # formula form the internet
    res = chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
    if not with_empty:
        next(res, None)
    if as_iterable:
        return res
    return list(res)


def continued_fraction_of_sqrt(x: int) -> List[int]:
    """
    returns the coefficients cycle of the continued fraction of sqrt(input).
    empty list if input is perfect square
    :param x: number to get continued fraction of its square
    :return: the coefficients cycle of the continued fraction of sqrt(input)
    """
    sqrt_x: float = math.sqrt(x)
    if sqrt_x.is_integer():
        return []
    s: Set[QPair] = set()  # set of all pairs of QPairs
    l: List[QPair] = list()  # list of these pairs, the result cycle
    # create the initial pair
    start_value: FracWithSqrt = FracWithSqrt(Frac(1), Frac(0), x)
    pair: QPair = start_value.split_int_nonint()
    # calculate the continued fractions until we get a repetition
    while pair not in s:
        s.add(pair)
        l.append(pair)
        # get new pair
        r: FracWithSqrt = pair.rem.flip()
        pair = r.split_int_nonint()
    # the whole parts of the pairs until the repetition in the cycle
    return [i.whole for i in l[l.index(pair):]]


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


def divisors_sum(n: int, including_i=True) -> List[int]:
    """
    :param n: max number for range (exclude it)
    :param including_i: should we include i itself in the sum of divisors
    :return: a list of the sum of divisors of all numbers from 0 to n-1
    """
    divs_sums = np.zeros(n, dtype='int32')
    if including_i:
        for i in range(1, len(divs_sums)):
            divs_sums[i::i] += i
    else:
        for i in range(1, len(divs_sums)):
            divs_sums[i] -= i
            divs_sums[i::i] += i
    return [i for i in divs_sums]


def fibonacci_number_by_index(index: int):
    """
    calculated fast using matrix multiplication and power, in log(n) time
    :param index: index of wanted fibonacci number
    :return: the number
    """
    if index == 0:
        return 0
    if index == 1 or index == 2:
        return 1

    def mult_mat(x: ((int, int), (int, int)), y: ((int, int), (int, int))) -> ((int, int), (int, int)):
        return ((x[0][0] * y[0][0] + x[0][1] * y[1][0], x[0][0] * y[0][1] + x[0][1] * y[1][1]),
                (x[1][0] * y[0][0] + x[1][1] * y[1][0], x[1][0] * y[0][1] + x[1][1] * y[1][1]))

    def power_mat(x, y) -> ((int, int), (int, int)):
        if y == 0:
            return (1, 0), (0, 1)  # identity mat
        temp = power_mat(x, y // 2)

        if y % 2 == 0:
            return mult_mat(temp, temp)
        else:
            return mult_mat(x, mult_mat(temp, temp))

    fib_mat = ((1, 1), (1, 0))  # the fibonacci matrix
    mat_n = power_mat(fib_mat, index - 2)
    return sum(mat_n[0])


def list_product(nums: List[int]):
    p = 1
    for x in nums:
        p *= x
    return p


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


def sieve_primes(n):
    flags = np.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, int(math.sqrt(n) + 1)):
        if flags[i]:
            flags[i * i::i] = False
    return list(np.flatnonzero(flags))


def sum_first_n(max_n: int):
    return ((max_n + 1) * max_n) // 2


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
