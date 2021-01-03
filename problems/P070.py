from libs.numbers_properties import same_digits
from libs.calculations import totient_euler_range


def ans():
    print("solution in about 45 seconds")
    n = 10 ** 7
    te_range = totient_euler_range(n)[2:]
    ll = [(i, int(te_range[i])) for i in range(2, len(te_range)) if same_digits(i, int(te_range[i]))]
    return min(ll, key=lambda p: p[0] / p[1])[0]
