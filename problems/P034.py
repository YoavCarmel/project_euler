from math import factorial


def ans():
    s = 0
    factorial_digits = {i: factorial(i) for i in range(10)}
    # as in question 30, we can see that the max is 2540169
    for i in range(3, 2540160):
        if i == sum_digit_factorial(i, factorial_digits):
            s += i
    return s


def sum_digit_factorial(x, factorial_digits):
    s = 0
    while x > 0:
        s += factorial_digits[x % 10]
        x //= 10
    return s
