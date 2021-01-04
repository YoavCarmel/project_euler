from typing import List

from libs.numbers_properties import num_size
from sympy import isprime


def ans():
    count: int = 4
    i: int = 7
    n: int = 1000000
    while i < n:
        i += max(forbidden_digits(i, [1, 3, 7, 9]), 2)
        if is_circular_prime(i):
            count += 1
    return count


def forbidden_digits(x: int, digits: List[int])->int:
    """
    increment the input number such that after the increment it contains only the input digits
    :param x: input number
    :param digits: allowed digits
    :return: the increment
    """
    x_str = str(x)
    for i in range(len(x_str)):
        if int(x_str[i]) not in digits:
            if i != len(x_str) - 1:
                return 10 ** (len(x_str) - i - 1)
    return 0


def is_circular_prime(x: int) -> bool:
    """
    :param x: input number
    :return: if x is a circular prime or not
    """
    n_size = num_size(x)
    for i in range(n_size):
        x = x // 10 + (x % 10) * 10 ** (n_size - 1)
        if not isprime(x):
            return False
    return True
