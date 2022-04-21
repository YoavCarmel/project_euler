from itertools import product
from math import log

import pytest

from libs.calculations.general import sum_first_n
from libs.types_converting import num_to_list


def digits_sum(x: int) -> int:
    s = 0
    while x > 0:
        s += x % 10
        x //= 10
    return s


def sum_digits_to_power_10(power_10, inclusive=False):
    """
    sum of the digits of all numbers up to power_10, of form 10**n
    """
    return sum_first_n(9) * round(log(power_10, 10)) * power_10 // 10 + int(inclusive)


def sum_digits_to_power_10_multiple(power_10_mult, inclusive=True):
    """
    sum of the digits of all numbers up to power_10_mult,  of form k*10**n
    """
    if power_10_mult == 0:
        return 0
    power_10 = 10 ** int(log(power_10_mult, 10))
    mult = power_10_mult // power_10
    return sum_digits_to_power_10(power_10) * mult + sum_first_n(mult - 1) * power_10 + mult * inclusive


def digits_sum_first_n(max_n: int, inclusive=True):
    """
    sum of the digits of first n numbers: [1,2,3,...,max_n]
    """
    digs = num_to_list(max_n)[::-1]
    s = 0
    for i, d in enumerate(digs):
        s += d * 10 ** i * sum(digs[i + 1:]) + sum_digits_to_power_10_multiple(d * 10 ** i)
    return s - int(not inclusive) * digits_sum(max_n)


@pytest.mark.parametrize("s, b", product([10, 100, 400, 2000, 5000, 10000, 123, 53253, 13232, 40402], [True, False]))
def test_digits_sum_first_n(s: int, b: bool):
    assert digits_sum_first_n(s, inclusive=b) == sum(digits_sum(i) for i in range(s + int(b)))
