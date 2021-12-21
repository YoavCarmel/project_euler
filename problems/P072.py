from libs.calculations.numbers_theory import totient_euler_range


def ans():
    d = 10 ** 6
    # for each d value, get the numbers that are coprimes with it, so it is a reduced fraction
    return sum(totient_euler_range(d)[2:])
