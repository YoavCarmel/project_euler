from math import sqrt

from tqdm import tqdm

from libs.calculations import sieve_primes


def ans():
    max_n = 10 ** 8
    primes = set(sieve_primes(max_n))
    s = 0
    """
    we know that num+1 should be a prime, because 1 if a divisors of num for all nums.
    that means, that we can iterate only over the primes-1, instead of the whole range.
    
    in addition, that means that num is even (except for 1), so num//2+2 must also be a prime.
    that means, that num//2 must be odd, so we get that num%4=2, so prime%4=3.
    we should remember to add 1 to the final sum
    
    num cannot be a square number because that means that d==n//d and (d+n//d) is even, so not prime.
    but this is obvious since num = 4k+2.
    """
    primes_to_iterate = primes.intersection(3 + i for i in range(0, max_n + 1, 4))
    primes_to_iterate = {p for p in primes_to_iterate if ((p - 1) // 2 + 2) in primes}
    for num_p1 in tqdm(primes_to_iterate):
        num = num_p1 - 1  # because n+1 must be a prime
        if check_for_num(num, primes):
            s += num
    return s + 1


def check_for_num(num, primes):
    for div in range(3, int(sqrt(num)) + 1):  # no need to check 1,2
        if num % div == 0 and (div + num // div) not in primes:
            return False
    return True
