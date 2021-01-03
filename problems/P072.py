from libs.calculations import totient_euler_range


def ans():
    d = 10**6
    return sum(totient_euler_range(d)[2:])
