from libs.numbers_properties import is_pandigital


def ans():
    m = 0
    i = 1
    while i < 500000:
        if concate_num(i) != 0:
            if concate_num(i) > m:
                m = concate_num(i)
        i += 1
    return m


def concate_num(x):
    n = 1
    s = ""
    while len(s) < 9:
        s += str(x * n)
        n += 1
    if len(s) == 9:
        if is_pandigital(int(s), 9):
            return int(s)
    return 0
