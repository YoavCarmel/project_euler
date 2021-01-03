from libs.numbers_properties import same_digits
from libs.calculations import totient_euler_range


def ans():
    print("solution in about 45 seconds")
    n = 10 ** 7
    l = totient_euler_range(n)[2:]
    ll = [(i, int(l[i])) for i in range(2, len(l)) if same_digits(i, int(l[i]))]
    return min(ll, key=lambda p: p[0] / p[1])[0]
