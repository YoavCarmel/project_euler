from sympy import isprime


def ans():
    primes_count = 0
    total_count = 1
    num = 1
    square_size = 3
    while True:
        h = square_size - 1
        for i in range(4):
            num += h
            if isprime(num):
                primes_count += 1
        total_count += 4
        if primes_count / total_count < 0.1:
            break
        square_size += 2
    return square_size
