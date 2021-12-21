from libs.calculations.numbers_operations import reverse_num
from libs.calculations.numbers_properties import is_palindrome


def ans():
    count: int = 0
    for i in range(10000):
        if is_lychrel_number(i):
            count += 1
    return count


def is_lychrel_number(x: int) -> int:
    """
    :param x: input number
    :return: True if the input number is a lychrel number within 50 iterations
    """
    for i in range(50):
        x = x + reverse_num(x)
        if is_palindrome(x):
            return False
    return True  # for number below 10,000
