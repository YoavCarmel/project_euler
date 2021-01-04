from math import factorial
from typing import Dict


def ans():
    s: int = 0
    factorial_digits: Dict[int, int] = {i: factorial(i) for i in range(10)}
    # as in question 30, we can see that the max is 2540169
    for i in range(3, 2540160):
        if i == sum_digit_factorial(i, factorial_digits):
            s += i
    return s


def sum_digit_factorial(x: int, factorial_digits: Dict[int, int]) -> int:
    """
    :param x: input number
    :param factorial_digits: known factorials of digits, to prevent repeated calculations
    :return: sum of factorials of digits
    """
    s: int = 0
    while x > 0:
        s += factorial_digits[x % 10]
        x //= 10
    return s
