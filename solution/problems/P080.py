from solution.libs.numbers_properties import digits_sum, is_square
from math import sqrt


def ans():
    return sum([sum_n_digits(i, 100) for i in range(100)])


def sum_n_digits(num, n):
    if is_square(num):
        return 0
    return digits_sum(square_root(num, n))


def square_root(num, digs):
    if is_square(num):
        return int(sqrt(num))
    res = 0
    for i in range(digs):
        res *= 10
        for j in range(1, 10):
            res += 1
            np = num * 10 ** (2 * i)
            if res ** 2 > np:
                res -= 1
                break
    return res
