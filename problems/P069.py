from sympy import nextprime


def ans():
    # we know that the totient decreases relative to n only when adding a new prime factor,
    # so just get the mx number of prime factors, that means that the res is a product of distinct prime factors
    n = 10 ** 6
    product = 2
    prime = 2
    while product < n:
        prime = nextprime(prime)
        product *= prime
    return product // prime
