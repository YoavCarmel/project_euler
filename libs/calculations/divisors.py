import numpy as np


def divisors_sum(n: int, including_itself=True) -> np.ndarray:
    """
    :param n: max number for range (exclude it)
    :param including_itself: should we include i itself in the sum of divisors
    :return: a list of the sum of divisors of all numbers from 0 to n-1
    """
    divs_sums = np.zeros(n, dtype='int32')
    if including_itself:
        for i in range(1, len(divs_sums)):
            divs_sums[i::i] += i
    else:
        for i in range(1, len(divs_sums)):
            divs_sums[2 * i::i] += i
    return divs_sums


def divisors_count(n: int, including_itself=True) -> np.ndarray:
    """
    :param n: max number for range (exclude it)
    :param including_itself: should we include i itself in the count of divisors
    :return: a list of the number of divisors of all numbers from 0 to n-1
    """
    divs_sums = np.zeros(n, dtype='int16')
    for i in range(1, n // 2 + 1):
        divs_sums[i::i] += 1
    divs_sums[n // 2 + 1:] += 1
    if not including_itself:
        divs_sums -= 1
    return divs_sums
