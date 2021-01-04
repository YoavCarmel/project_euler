from libs.calculations import base2
from libs.numbers_properties import is_palindrome


def ans():
    s = 0
    for i in range(1000000):
        # check if palindrome in both base 10 and base 2
        if is_palindrome(i) and is_palindrome(base2(i)):
            s += i
    return s
