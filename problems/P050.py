from typing import List, Set

from sympy import primerange


def ans():
    limit: int = 10 ** 6
    primes: List[int] = list(primerange(1, limit + 1))
    # get sums of all primes from 2 to i
    primes_sums: List[int] = list()
    primes_sums.append(0)
    # get set of all primes of this range
    primes_set: Set[int] = set(primes)
    for i in range(len(primes)):
        primes_sums.append(primes_sums[-1] + primes[i])
    for window_length in range(len(primes_sums) - 1, -1, -1):
        for i in range(len(primes)-window_length+1):
            primes_window_sum = primes_sums[i + window_length]-primes_sums[i]
            if primes_window_sum > limit:
                break
            if primes_window_sum in primes_set:
                return primes_window_sum
