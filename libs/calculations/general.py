import math
from functools import reduce
from itertools import chain, combinations
from operator import mul
from typing import List, Iterable, Set

import numpy as np

from libs.objects.frac import Frac
from libs.objects.frac_with_sqrt import QPair, FracWithSqrt


def multinom(nums: List[int]) -> int:
    """
    calculate the multinom of the input numbers, the numerator is their sum
    :param nums: the numbers to calculate the multinom of
    :return: their multinom
    """
    top = math.factorial(sum(nums))
    bottom = list_product([math.factorial(num) for num in nums])
    return top // bottom


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


def smallest_number_with_digit_sum(n: int) -> int:
    """
    :param n: wanted digits sum
    :return: smallest number with input digits sum
    """
    return int(str(n % 9) + "9" * (n // 9))


def power_set(iterable: Iterable, with_empty: bool = True) -> Iterable:
    """
    returns the power set of the input iterable
    :param iterable: the iterable to create its power set
    :param with_empty: include/exclude the empty set
    :return: the power set, as iterable
    """
    s = list(iterable)
    # formula form the internet
    res = chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
    if not with_empty:
        next(res, None)
    return res


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


def divisors_sum(n: int, including_itself=True) -> List[int]:
    """
    :param n: max number for range (exclude it)
    :param including_itself: should we include i itself in the sum of divisors
    :return: a list of the sum of divisors of all numbers from 0 to n-1
    """
    divs_sums = np.zeros(n, dtype='int32')
    for i in range(1, len(divs_sums)):
        divs_sums[i::i] += i
    if not including_itself:
        divs_sums -= np.arange(len(divs_sums))
    return list(divs_sums)


def fibonacci_number_by_index(index: int):
    """
    calculated fast using matrix multiplication and power, in log(n) time
    :param index: index of wanted fibonacci number
    :return: the number

    NOTE: cant use numpy here because numbers are too big
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
    return reduce(mul, nums, 1)


def sum_first_n(max_n: int):
    """
    sum of first n numbers: [1,2,3,...,max_n]
    """
    return ((max_n + 1) * max_n) // 2


def diffs_list(lst: List[int]) -> List[int]:
    """
    :param lst: a list of numbers
    :return: a list of the differences between each adjacent pair
    """
    lst_np = np.array(lst)
    return list(lst_np[:-1] - lst_np[1:])


def pascal_triangle(n_rows: int, mod: int = None) -> np.ndarray:
    tri = np.zeros((n_rows, n_rows), dtype="uint64")
    tri[0][0] = 1
    for r in range(1, n_rows):
        tri[r] = tri[r - 1]
        tri[r, 1:] += tri[r - 1, :-1]
        if mod is not None:
            tri[r] %= mod
    return tri
