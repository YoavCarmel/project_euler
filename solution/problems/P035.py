from solution.libs.numbers_properties import num_size
from sympy import isprime


def ans():
    count = 4
    i = 7
    n = 1000000
    while i < n:
        i += max(forbidden_digit(i, [1, 3, 7, 9]), 2)
        if is_circular_prime(i):
            count += 1
    return count


def forbidden_digit(x, digits):
    x_str = str(x)
    for i in range(len(x_str)):
        if int(x_str[i]) not in digits:
            if i != len(x_str) - 1:
                return 10 ** (len(x_str) - i - 1)
    return 0


def is_circular_prime(x):
    l = num_size(x)
    for i in range(l):
        x = x // 10 + (x % 10) * 10 ** (l - 1)
        if not isprime(x):
            return False
    return True
