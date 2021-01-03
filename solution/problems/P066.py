from math import sqrt, inf
from solution.libs.numbers_properties import is_square


# algorithm is copied from the internet, because i could not find any place to learn about pell equations from
def ans():
    result = 0
    pmax = 0
    for D in range(2, 1000 + 1):
        if is_square(D):
            continue
        limit = int(sqrt(D))

        m = 0
        d = 1
        a = limit
        num1 = 1
        num = a
        den1 = 0
        den = 1
        while num ** 2 - D * den ** 2 != 1:
            m = d * a - m
            d = (D - m * m) // d
            a = (limit + m) // d
            num2 = num1
            num1 = num
            den2 = den1
            den1 = den

            num = a * num1 + num2
            den = a * den1 + den2

        if num > pmax:
            pmax = num
            result = D
    return result
