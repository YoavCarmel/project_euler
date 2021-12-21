from libs.calculations.numbers_properties import digits_sum
from math import factorial


def ans():
    # just calculate the factorial of 100 and its digits sum
    return digits_sum(factorial(100))
