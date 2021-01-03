from tqdm import trange, tqdm
from solution.libs.numbers_operations import list_to_num, num_to_list
from solution.libs.numbers_properties import digs_count, num_size
from solution.libs.calculations import multinom
from itertools import combinations_with_replacement, permutations


def ans():
    """max_i = 10 ** 7
    return f1(max_i)"""
    max_10_power = 7
    return f2(max_10_power)


def f1(max_i):
    print("takes about 30 seconds")
    gets_to_89 = {89}
    gets_to_1 = {1}
    for i in trange(1, max_i + 1):
        chain = list()
        j = i
        while j not in gets_to_89 and j not in gets_to_1:
            chain.append(j)
            j = sum_square_digs(j)
        if j in gets_to_89:
            gets_to_89.update(chain)
        else:  # gets to 1
            gets_to_1.update(chain)
    return len(gets_to_89)


def f2(max_10_power):
    # the main point is that numbers with same digits will have the same result
    gets_to_89 = set()
    digs = list(range(10))
    for t in combinations_with_replacement(digs, max_10_power):
        ti = list_to_num(t)
        if ti == 0:
            continue
        j = ti
        while j != 89 and j != 1:
            j = sum_square_digs(j)
        if j == 89:
            gets_to_89.add(ti)
    return sum([multinom(list(digs_count(i).values()) + [max_10_power - num_size(i)]) for i in gets_to_89])
    # the [max_10_power - num_size(i)] is for zeros


def sum_square_digs(n):
    s = 0
    while n > 0:
        s += (n % 10) ** 2
        n //= 10
    return s
