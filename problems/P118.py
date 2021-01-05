from itertools import permutations, combinations
from typing import Set, FrozenSet, List, Dict

from libs.types_converting import list_to_num
from libs.numbers_properties import num_size

from sympy import isprime


def ans():
    s: Set[FrozenSet[int]] = set()
    rec(set(range(1, 9 + 1)), dict(), list(), s)
    return len(s)


def rec(digs_left: Set[int], primes: Dict[FrozenSet[int], Set[int]], current_solution: List[int],
        all_solutions: Set[FrozenSet[int]]):
    """
    :param digs_left: the digits left to handle in set
    :param primes: primes from digits sets, that already calculated
    :param current_solution: the current "set"
    :param all_solutions: all calculated solutions
    """
    if len(digs_left) == 0:
        all_solutions.add(frozenset(current_solution))
    start = 1 if len(current_solution) == 0 else num_size(current_solution[-1])
    for i in range(start, len(digs_left) + 1):
        for c in combinations(digs_left, i):
            fs_c = frozenset(c)
            if fs_c not in primes:
                primes[fs_c] = get_primes_from_digits(fs_c)
            for p in primes[fs_c]:
                rec(digs_left.difference(c), primes, current_solution + [p], all_solutions)


def get_primes_from_digits(digs) -> Set[int]:
    """
    :param digs: digits to handle
    :return: all primes that can be created from these digits
    """
    if len(digs) == 1:
        return {2, 3, 5, 7}.intersection(digs)
    # else, only the digits [1,3,7,9] can be the units digit
    units_digits = {1, 3, 7, 9}.intersection(digs)
    if len(units_digits) == 0:
        # no possible solution
        return set()
    s = set()
    for p in permutations(digs, len(digs) - 1):
        ltm_p = list_to_num(p)
        # create all digits apart from the units digit
        for units_digit in units_digits.difference(p):
            if isprime(ltm_p * 10 + units_digit):
                s.add(ltm_p * 10 + units_digit)
    return s
