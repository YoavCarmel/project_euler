from libs.calculations import totient_euler
from sympy import nextprime


def ans():
    n = 10 ** 6
    return smart(n)


def brute(n):
    max_n = 2
    max_t = 0
    for i in range(2, n + 1):
        t = i / totient_euler(i)
        if t > max_t:
            max_t = t
            max_n = i
    return max_n


def smart(n):
    product = 2
    prime = 2
    while product < n:
        prime = nextprime(prime)
        product *= prime
    return product // prime
