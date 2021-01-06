from collections import defaultdict
from itertools import combinations
from typing import Dict, Tuple, Set, List

from sympy import primerange

from libs.types_converting import num_to_list


def ans():
    # get all primes
    four_digits_primes: List[int] = list(primerange(10 ** 3, 10 ** 4))
    # split primes by digits
    primes_by_digs: Dict[Tuple[int, ...], Set[int]] = defaultdict(set)
    for prime in four_digits_primes:
        primes_by_digs[tuple(sorted(num_to_list(prime)))].add(prime)
    results: List[str] = []
    # for all 4-digits perms that have 3 or more primes
    for four_digs, primes in primes_by_digs.items():
        if len(primes) < 3:
            continue
        for triple in combinations(primes, 3):
            ts: Tuple[int, ...] = tuple(sorted(triple))
            # if arithmetic sequence, add to results
            if ts[2] - ts[1] == ts[1] - ts[0]:
                results.append(str(ts[0]) + str(ts[1]) + str(ts[2]))
    return results[1]
