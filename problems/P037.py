from libs.numbers_properties import contains_digits, num_size
from sympy import isprime


def ans():
    count = 0
    i = 9
    s = 0
    while count < 11:
        if not contains_digits(i, [4, 6, 8, 0]):
            if both_sides_prime(i):
                count += 1
                s += i
        i += 2
    return s


def both_sides_prime(x: int) -> bool:
    """
    :param x: input number
    :return: True if input number is both right and left prime
    """
    return right_prime(x) and left_prime(x)


def right_prime(x: int) -> bool:
    """
    :param x: input number
    :return: True if input number is a right prime
    """
    while x > 0:
        if not isprime(x):
            return False
        x //= 10
    return True


def left_prime(x: int) -> bool:
    """
    :param x: input number
    :return: True if input number is a left prime
    """
    while x > 0:
        if not isprime(x):
            return False
        x = x % (10 ** (num_size(x) - 1))
    return True
