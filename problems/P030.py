def ans():
    """
    using math, the max number that can may be represented by sum of his digits raised to 5th power
    is:(also can solve when 10^n>n*9^5)
    number of digits | max sum(all digits are 9)
    1                   9^5=59049
    2                   2*9^5=118092
    3                   3*9^5=177147
    4                   4*9^5=236196
    5                   5*9^5=295245
    6                   6*9^5=354294(has same number of digits)
    7                   7*9^5=413343(does not have enough digits)
    so max number is 354294(of course that is not the real maximum, but we know that no number above it can do it.
    so check all number smaller than this bound
    """
    s: int = 0
    for i in range(2, 354294):
        if i == sum_5_power_digits(i):
            s += i
    return s


def sum_5_power_digits(x: int) -> int:
    """
    :param x: input number
    :return: sum of each digit to the power of 5
    """
    s: int = 0
    while x > 0:
        s += (x % 10) ** 5
        x //= 10
    return s
