from math import factorial

from libs.calculations.numbers_properties import digits_sum


def ans():
    # just calculate the factorial of 100 and its digits sum
    return digits_sum(factorial(100))
