def ans():
    s = 0
    for a in range(3, 1000 + 1):
        s += fa(a)
    return s


def fa(a):
    """
    for even n always returns 2.
    for odd n, the calculation equals (2*n*a)%(a**2)
    """
    m = 2
    ap2 = a ** 2
    at2 = a * 2
    s = 0
    for n in range(1, 2 * a + 1, 2):
        s = (s + at2) % ap2
        m = max(m, s)
    return m
