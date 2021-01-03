from itertools import permutations, combinations
from typing import Set, FrozenSet, List, Dict

from libs.types_converting import list_to_num
from libs.numbers_properties import num_size

from sympy import isprime


def ans():
    l = set()
    rec(set(range(1, 9 + 1)), dict(), list(), l)
    return len(l)


def rec(digs_left: Set[int], primes: Dict[FrozenSet[int], Set[int]], current_solution: List[int],
        all_solutions: Set[FrozenSet[int]]):
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
    s = set()
    for p in permutations(digs):
        ltm_p = list_to_num(p)
        if isprime(ltm_p):
            s.add(ltm_p)
    return s
