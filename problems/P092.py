from itertools import combinations_with_replacement

from libs.calculations.combinatorics import multinom
from libs.calculations.numbers_operations import list_to_num
from libs.calculations.numbers_properties import digs_count, num_size


def ans():
    max_10_power = 7
    # the main point is that numbers with same digits will have the same result
    gets_to_89 = set()
    for t in combinations_with_replacement(range(10), max_10_power):
        ti = list_to_num(t)
        if ti == 0:
            continue
        j = ti
        while j != 89 and j != 1:
            j = sum_square_digs(j)
        if j == 89:
            # only add the starting number and not the whole chain
            gets_to_89.add(ti)
    return sum([multinom(list(digs_count(i).values()) + [max_10_power - num_size(i)]) for i in gets_to_89])
    # the [max_10_power - num_size(i)] is for zeros


def sum_square_digs(n):
    s = 0
    while n > 0:
        s += (n % 10) ** 2
        n //= 10
    return s
