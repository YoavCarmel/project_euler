from solution.libs.numbers_properties import same_digits
from sympy import isprime


def ans():
    four_digits_primes = []
    results = []
    for i in range(10 ** 3, 10 ** 4):
        if isprime(i):
            same_digits_primes = []
            for j in four_digits_primes:
                if same_digits(i, j):
                    same_digits_primes.append(j)
            four_digits_primes.append(i)
            if len(same_digits_primes) >= 2:
                for p1 in range(len(same_digits_primes)):
                    for p2 in range(p1+1, len(same_digits_primes)):
                        if same_digits_primes[p2] - same_digits_primes[p1] == i - same_digits_primes[p2]:
                            results.append(str(same_digits_primes[p1])+str(same_digits_primes[p2])+str(i))
    return results[1]
