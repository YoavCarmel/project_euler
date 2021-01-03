from libs.numbers_properties import is_pandigital


def ans():
    n = 10000
    good_nums = set([i for i in range(1, n + 1) if good_num(i)])

    products = []
    for a in good_nums:
        for b in [i for i in good_nums if i<1000]:
            p = a * b
            if p in good_nums:
                if good_trio(a, b, p):
                    products.append(p)
    # return sum(set(products))
    return sum(set(products))


def good_num(x):
    digs = set()
    while x > 0:
        d = x % 10
        if d == 0:
            return False  # should not have 0
        if d in digs:
            return False  # should not have repeated digits
        else:
            digs.add(d)
        x //= 10
    return True


def good_trio(a, b, p):
    final_digits = str(a) + str(b) + str(p)
    if is_pandigital(int(final_digits), 9):
        return True
    return False
