from libs.calculations.numbers_properties import is_palindrome


def ans():
    m: int = -1
    # get the maximum, we can start from 900,900 because the max is for sure in there
    for i in range(900, 1000):
        for j in range(i, 1000):
            if is_palindrome(i * j):
                m = max(m, i * j)
    return m
