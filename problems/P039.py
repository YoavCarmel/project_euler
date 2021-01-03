from math import sqrt
from libs.numbers_properties import is_int


def ans():
    count_list = []
    max_p = 0
    for i in range(1001):
        count_list.append(0)
    for a in range(1, 500):
        for b in range(1, a):
            c = sqrt(a ** 2 + b ** 2)
            if is_int(c):
                c = int(c)
                p = a + b + c
                if p <= 1000:
                    count_list[p] += 1
    for i in range(1001):
        if count_list[i] > count_list[max_p]:
            max_p = i
    return max_p
