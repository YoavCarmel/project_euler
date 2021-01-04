from libs.numbers_properties import is_pandigital


def ans():
    m: int = 0
    i: int = 1
    # after mult by 2 and concatenate, we should have at mosts 9 digits, so this is a good upper bound
    while i < 10000:
        if concatenate_num(i):
            m = max(m, concatenate_num(i))
        i += 1
    return m


def concatenate_num(x: int) -> int:
    """
    concatenate multiples of the number until we reach length 9
    :param x: input number
    :return: the concatenated length 9 pandigital, 0 if false
    """
    n: int = 1
    s: str = ""
    while len(s) < 9:
        s += str(x * n)
        n += 1
    if len(s) == 9:
        if is_pandigital(int(s), 9):
            return int(s)
    return 0
