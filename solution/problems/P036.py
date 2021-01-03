from solution.libs.calculations import base2
from solution.libs.numbers_properties import is_palindrome


def ans():
    s = 0
    for i in range(1000000):
        if is_palindrome(i) and is_palindrome(base2(i)):
            s += i
    return s
