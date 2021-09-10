from collections import defaultdict
from functools import lru_cache
from math import log
from typing import Dict, List, Set, Tuple, Optional

import pytest
from pulp import LpProblem, lpSum, LpVariable, LpMaximize
from sympy import primefactors

from libs.calculations import sieve_primes

IntsTuple = Tuple[int, ...]


class ImprovingTuplesData:
    def __init__(self, n, primes):
        self.n: int = n
        self.primes: List[int] = primes
        self.tuple_to_profit: Dict[IntsTuple, int] = dict()
        self.primes_to_tuples: Dict[int, Set[IntsTuple]] = defaultdict(set)

    def add_tuple(self, t: IntsTuple, profit: int):
        self.tuple_to_profit[t] = profit
        for val in t:
            self.primes_to_tuples[val].add(t)

    def naive_primes_powers_sum(self) -> int:
        """
        :return: sum of the biggest power of each prime that is <= n
        """
        return sum([get_max_for_prime(self.n, p) for p in self.primes])


def ans():
    """
    The idea:
    First, get a list of all primes in the range (1,n).
    Then we want to generate co-prime groups in a smart way,
    that minimizes the number of groups that are for sure worse than other groups.

    First, for each pair of primes (sorted),
    check if their product is still less than n - if merging them is even valid,
    and if the sum of the max possible values out of each of them is less than
    the max possible num from these factors that is still <=n, which means that merging them increases the sum.
    Obviously, if their product is bigger than n, we can stop the inner loop, and this can be optimized even more
    by checking if this was the first inner iteration, and if so, we can stop the outer loop.
    For each merged pair we keep the profit of the merging (in a dict):
    (the max value of these factors that is <= n) minus (the sum of the max possible values out of each of them)
    Do the same for triples, checking whether the max value for merging all 3 of them is better than any other
    combination of sums.
    We can basically do this generically for any lengths tuples, but i could not figure out how to do this
    without messing with nasty combinatorics, so i created thee same process for quads,
    which resulted in 0 improving quads, so i knew that we only need size 2,3 and not more than that.
    The code for quads is still in the solution file but i dont use it because it is a waste of run time.
    NOTE: running for 2*10**6, i found that there are indeed ~20 numbers that come from quads, so my solution is NOT
    generic, and who knows, maybe there are even pentas for a very large n value. But this is not the problem here.

    Now we have a group of values (the dict values) that we should take a subgroup of it with the biggest sum possible,
    such that there are no two chosen values that their keys share a number.
    This is a classic Linear Programming problem.
    Define:
        variables: each of the values should get a variable that is a boolean bi - chosen or not
        optimization: optimize the sum of vi*bi
        restrictions: no 2 values with a shared prime factors should both be chosen
    NOTE: the whole problem could have been solved using this approach, but the preprocessing reduces the complexity
    of the LP problem by A LOT

    At the end, combine the result of the LP model with the base value of the max power of each prime,
    and dont forget to add 1 as it is not a part of any prime calculation!

    Optimization result:
    only 4654 primes out of 17984 used to improve.
    only 21218 total numbers in LP out of 200000.
    """
    n = 2 * 10 ** 5
    primes: List[int] = sieve_primes(n)
    data = improving_tuples(n, primes)
    res = linear_programming_sol(data)
    return res


def improving_tuples(n: int, primes: List[int]) -> ImprovingTuplesData:
    result: ImprovingTuplesData = ImprovingTuplesData(n, primes)
    improving_pairs(result)
    improving_triples(result)
    return result


def improving_pairs(data: ImprovingTuplesData) -> int:
    """
    :param data: the data about the run
    :return: number of pairs added
    """
    c = 0
    for i, p in enumerate(data.primes):
        break_first = False  # if first inner loop broke on first iteration, stop the outer loop
        for j, p2 in enumerate(data.primes[i + 1:]):
            if p * p2 > data.n:  # stop the inner loop
                if j == 0:
                    break_first = True  # mark that inner loop broke on first iteration
                break
            profit = is_improving_pair(data.n, p, p2)
            if profit is not None:
                c += 1
                data.add_tuple((p, p2), profit)
        if break_first:
            break
    return c


def improving_triples(data: ImprovingTuplesData) -> int:
    """
    :param data: the data about the run
    :return: number of triples added
    """
    c = 0
    for i, p1 in enumerate(data.primes):
        break_first = False  # if second loop broke on first iteration, stop the first loop
        for j, p2 in enumerate(data.primes[i + 1:]):
            if p1 * p2 > data.n:  # stop the second loop
                if j == 0:
                    break_first = True  # mark that second loop broke on first iteration
                break
            break_second = False
            for k, p3 in enumerate(data.primes[i + j + 2:]):
                if p1 * p2 * p3 > data.n:  # stop the third loop
                    if k == 0:
                        break_second = True
                    break
                profit = is_improving_triple(data.n, p1, p2, p3)
                if profit is not None:
                    data.add_tuple((p1, p2, p3), profit)
                    c += 1
            if break_second:
                break
        if break_first:
            break
    return c


def improving_quads(data: ImprovingTuplesData) -> int:
    """
    :param data: the data about the run
    :return: number of quads added
    """
    c = 0
    for i1, p1 in enumerate(data.primes):
        break_first = False  # if second loop broke on first iteration, stop the first loop
        for i2, p2 in enumerate(data.primes[i1 + 1:]):
            if p1 * p2 > data.n:  # stop the second loop
                if i2 == 0:
                    break_first = True  # mark that second loop broke on first iteration
                break
            break_second = False
            for i3, p3 in enumerate(data.primes[i1 + i2 + 2:]):
                if p1 * p2 * p3 > data.n:  # stop the third loop
                    if i3 == 0:
                        break_second = True
                    break
                break_third = False
                for i4, p4 in enumerate(data.primes[i1 + i2 + i3 + 3:]):
                    if p1 * p2 * p3 * p4 > data.n:  # stop the fourth loop
                        if i4 == 0:
                            break_third = True
                        break
                    profit = is_improving_quad(data.n, p1, p2, p3, p4)
                    if profit is not None:
                        data.add_tuple((p1, p2, p3, p4), profit)
                        c += 1
                if break_third:
                    break
            if break_second:
                break
        if break_first:
            break
    return c


@lru_cache(maxsize=None)
def prime_factors_cached(num: int):
    """
    wrap sympy's primefactors function with a cache
    :param num: input number
    :return: distinct prime factors list of the num
    """
    return primefactors(num)


@lru_cache(maxsize=None)
def get_max_for_prime(n: float, p: int):
    """
    :param n: limit
    :param p: prime
    :return: max power value (the result of the power) that is <= n
    """
    return p ** int(log(n, p))


def get_max_for_primes(n: int, primes: List[int], start: int = 1):
    """
    :param n: limit
    :param primes: a list of distinct primes, sorted from smallest to biggest
    :param start: already calculated product
    :return: the highest number that is <= n, that its prime factors are exactly the input primes list
    """
    if len(primes) == 1:  # stopping condition
        return get_max_for_prime(n / start, primes[0])
    # else, run recursively:
    biggest_prime = primes[-1]
    if n / start < biggest_prime:
        return 0  # could not fit all numbers of the list
    # go over all powers of biggest_prime that can still fit in the n limit
    return max(get_max_for_primes(n, primes[:-1], start * biggest_prime ** power) * biggest_prime ** power for power in
               range(1, int(log(n / start, biggest_prime)) + 1))


@lru_cache(maxsize=None)
def get_max_for_composite(n: int, c: int):
    """
    :param n: limit
    :param c: composite
    :return: the highest number that is <= n, that its prime factors are exactly the primes that make up c
    """
    return get_max_for_primes(n, prime_factors_cached(c))


@lru_cache(maxsize=None)
def max_value_for_num_prime_factors(n: int, num: int):
    """
    :param n: limit
    :param num: input number
    :return: max value that can be made from the prime factors of num
    """
    return sum(get_max_for_prime(n, p) for p in prime_factors_cached(num))


def is_improving_pair(n, num1, num2) -> Optional[int]:
    """
    if the sum of the max values for num1,num2 is smaller than the max value for num1*num2, merging is better
    :return: the merge value profit if it is, None if not
    """
    pair_value = get_max_for_composite(n, num1 * num2)
    s = max_value_for_num_prime_factors(n, num1)
    if s + num2 >= pair_value:
        return None  # stop now, dont have to calculate the rest
    s += max_value_for_num_prime_factors(n, num2)
    if s < pair_value:
        return pair_value - s  # improving. return profit
    return None  # not improving. return "False"


def is_improving_triple(n, p1, p2, p3) -> Optional[int]:
    """
    if the sum of the max values for p1,p2,p3 is smaller than any other combination, merging is better
    :return: the merge value profit if it is, None if not
    """
    together = get_max_for_primes(n, [p1, p2, p3])
    mp1, mp2, mp3 = get_max_for_prime(n, p1), get_max_for_prime(n, p2), get_max_for_prime(n, p3)
    alone = mp1 + mp2 + mp3
    if alone > together:
        return None
    mp1p2 = get_max_for_composite(n, p1 * p2)
    p1p2 = mp1p2 + mp3
    if p1p2 > together:
        return None
    mp1p3 = get_max_for_composite(n, p1 * p3)
    p1p3 = mp1p3 + mp2
    if p1p3 > together:
        return None
    mp2p3 = get_max_for_composite(n, p2 * p3)
    p2p3 = mp2p3 + mp1
    if p2p3 > together:
        return None
    return together - max([alone, mp1p2, mp1p3, mp2p3])


def is_improving_quad(n, p1, p2, p3, p4) -> Optional[int]:
    """
    if the sum of the max values for p1,p2,p3 is smaller than any other combination, merging is better
    :return: the merge value profit if it is, None if not
    """
    together = get_max_for_primes(n, [p1, p2, p3, p4])
    mp1 = get_max_for_prime(n, p1)
    mp2 = get_max_for_prime(n, p2)
    mp3 = get_max_for_prime(n, p3)
    mp4 = get_max_for_prime(n, p4)
    # 1,1,1,1
    if mp1 + mp2 + mp3 + mp4 > together:
        return None
    # 2,1,1
    mp1p2 = get_max_for_composite(n, p1 * p2)
    if mp1p2 + mp3 + mp4 > together:
        return None
    mp1p3 = get_max_for_composite(n, p1 * p3)
    if mp1p3 + mp2 + mp4 > together:
        return None
    mp1p4 = get_max_for_composite(n, p1 * p4)
    if mp1p4 + mp2 + mp3 > together:
        return None
    mp2p3 = get_max_for_composite(n, p2 * p3)
    if mp2p3 + mp1 + mp4 > together:
        return None
    mp2p4 = get_max_for_composite(n, p2 * p4)
    if mp2p4 + mp1 + mp3 > together:
        return None
    mp3p4 = get_max_for_composite(n, p3 * p4)
    if mp3p4 + mp1 + mp2 > together:
        return None
    # 2,2
    if mp1p2 + mp3p4 > together:
        return None
    if mp1p3 + mp2p4 > together:
        return None
    if mp1p4 + mp2p3 > together:
        return None
    # 3,1
    mp1p2p3 = get_max_for_composite(n, p1 * p2 * p3)
    if mp1p2p3 + mp4 > together:
        return None
    mp1p2p4 = get_max_for_composite(n, p1 * p2 * p4)
    if mp1p2p4 + mp3 > together:
        return None
    mp1p3p4 = get_max_for_composite(n, p1 * p3 * p4)
    if mp1p3p4 + mp2 > together:
        return None
    mp2p3p4 = get_max_for_composite(n, p2 * p3 * p4)
    if mp2p3p4 + mp1 > together:
        return None
    # 4 is better!
    return together - max(
        [mp1 + mp2 + mp3 + mp4, mp1p2 + mp3 + mp4, mp1p3 + mp2 + mp4, mp1p4 + mp2 + mp3, mp2p3 + mp1 + mp4,
         mp2p4 + mp1 + mp3, mp3p4 + mp1 + mp2, mp1p2 + mp3p4, mp1p3 + mp2p4, mp1p4 + mp2p3, mp1p2p3 + mp4,
         mp1p2p4 + mp3, mp1p3p4 + mp2, mp2p3p4 + mp1])


def linear_programming_sol(data: ImprovingTuplesData) -> int:
    """
    solve using linear programming
    """
    # for very small n values:
    if len(data.tuple_to_profit) == 0:
        return data.naive_primes_powers_sum() + 1
    # General case:
    # init the model
    model = LpProblem(name="max_subgroup_sum", sense=LpMaximize)
    # create variables:
    merged_values: Dict[IntsTuple, LpVariable] = {p: LpVariable(name=f"var({p})", cat="Binary") for p in
                                                  data.tuple_to_profit}
    # add constraints:
    for prime, tuples in data.primes_to_tuples.items():
        # each prime number should appear only once!
        model += (lpSum([merged_values[t] for t in tuples]) <= 1, f"cons({prime})")
    # add objective - the value each pair gives us if it is chosen
    model += lpSum([profit * merged_values[pair] for pair, profit in data.tuple_to_profit.items()])
    # Solve the optimization problem
    model.solve()

    res = int(model.objective.value())  # total profit over the base naive sum of powers of primes
    return res + data.naive_primes_powers_sum() + 1


@pytest.mark.parametrize("inputs, output", [((2, 2), 2), ((8, 2), 8), ((27, 3), 27), ((30, 3), 27), ((1, 2), 1)])
def test_get_max_for_prime(inputs, output):
    n, p = inputs
    assert get_max_for_prime(n, p) == output


@pytest.mark.parametrize("inputs, output",
                         [((2, 2), 2), ((8, 2), 8), ((10, 2), 8), ((20, 6), 18), ((24, 6), 24), ((125, 30), 120)])
def test_get_max_for_composite(inputs, output):
    n, c = inputs
    assert get_max_for_composite(n, c) == output
