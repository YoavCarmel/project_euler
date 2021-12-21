from libs.calculations.numbers_properties import digits_sum, is_square
from math import sqrt


def ans():
    return sum([sum_n_digits(i, 100) for i in range(100)])


def sum_n_digits(num: int, n: int) -> int:
    """
    :param num: input number
    :param n: number of digits
    :return: 0 is perfect square, else sum of first n digits of sqrt(num)
    """
    if is_square(num):
        return 0
    return digits_sum(square_root(num, n))


def square_root(num: int, digs: int) -> int:
    """
    :param num: input number
    :param digs: number of wanted digits
    :return: first "digs" digits in the square root of num including digits before and after the decimal point
    """
    if is_square(num):
        return int(sqrt(num))
    res = 0
    for i in range(digs):
        res *= 10
        for j in range(1, 10):
            # add until we pass the square
            res += 1
            np = num * 10 ** (2 * i)
            if res ** 2 > np:
                # too much, go back 1 and go for next digit to get more accurate
                res -= 1
                break
    return res
