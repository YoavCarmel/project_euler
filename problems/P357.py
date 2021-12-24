import math
from math import sqrt

import numpy as np
from tqdm import tqdm


def ans():
    max_n = 10 ** 8
    s = 0
    """
    we know that num+1 should be a prime, because 1 is a divisors of num for all nums.
    that means, that we can iterate only over the primes-1, instead of the whole range.

    in addition, that means that num is even (except for 1), so num//2+2 must also be a prime.
    that means, that num//2 must be odd, so we get that num%4=2, so prime%4=3.
    we should remember to add 1 to the final sum
    
    all of the prime factors of num should be of power 1, otherwise p is both in div and num//div so their sum
    is divisible by p and num is invalid.
    """
    primes, possibles = primes_and_possible_numbers(max_n)
    primes = primes[primes < max_n // 2 + 2]
    primes = set(primes)
    # ((p - 1) // 2 + 2) = num // 2 + 2 which should be in primes
    possibles_transformation = (possibles - 1) // 2 + 2
    possibles_to_iterate = [p for p, p_t in zip(possibles, possibles_transformation) if p_t in primes]
    for num_p1 in tqdm(possibles_to_iterate):
        num = num_p1 - 1
        divs = divisors(num)
        if set(divs + num // divs) <= primes:
            s += num
    return s + 1


def primes_and_possible_numbers(n) -> (np.ndarray, np.ndarray):
    """
    returns:
    a list of all primes
    a list of numbers that may be valid using the conditions i found.
    """
    flags = np.ones(n, dtype=bool)
    flags[0] = flags[1] = False
    for i in range(2, int(math.sqrt(n) + 1)):
        if flags[i]:
            """
            you may think we should start at i instead of i*i and we are skipping nums this way,
            but notice that we are skipping nums like 2i, 3i, ..., ki
            with k<i so that has already been taken care of with k
            """
            flags[i * i::i] = False
    all_primes = np.flatnonzero(flags)
    # calculate the possible numbers
    # p%3=4
    flags[1::4] = False
    flags[2] = False
    # also, eliminate primes s.t p-1 has a prime factor with a power>1
    for i in range(2, int(math.sqrt(n) + 1)):
        flags[i * i + 1::i * i] = False
    possibles = np.flatnonzero(flags)
    return all_primes, possibles


def divisors(n):
    a = np.arange(3, int(sqrt(n)) + 1, dtype="uint16")
    a_d = n / a
    return a[a_d == a_d.astype(int)]
