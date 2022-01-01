import math
from typing import List

from libs.calculations.lists_operations import list_product


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
