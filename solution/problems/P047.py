from sympy import primefactors


def ans():
    wanted = 4
    i = 1
    while True:
        if len(primefactors(i)) == wanted and len(primefactors(i + 1)) == wanted and \
                len(primefactors(i + 2)) == wanted and len(primefactors(i + 3)) == wanted:
            return i
        i += 1
