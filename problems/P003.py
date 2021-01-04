from sympy import primefactors


def ans():
    # just return the max of the prime factors of the number
    return max(primefactors(600851475143))
