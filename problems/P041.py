from libs.numbers_properties import is_pandigital, num_size
from sympy import isprime


def ans():
    # notice: every 9 digit and 8 digit pandigital number is divisible by 3, thus not prime
    i = 8 * (10 ** 6)
    while True:
        if isprime(i) and is_pandigital(i, num_size(i)):
            return i
        i -= 1
