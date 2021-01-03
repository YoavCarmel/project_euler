from objects.frac import Frac


def ans():
    max_d = 10 ** 6
    fractions = set()
    for i in range(1, max_d + 1):
        fractions.add(Frac((3 * i) // 7, i))
    fractions = sorted(fractions)
    i = fractions.index(Frac(3, 7))
    return fractions[i - 1].n
