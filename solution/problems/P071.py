from solution.objects.frac import Frac


def ans():
    max_d = 10 ** 6
    l = set()
    for i in range(1, max_d + 1):
        l.add(Frac((3 * i) // 7, i))
    l = sorted(l)
    i = l.index(Frac(3, 7))
    return l[i - 1].n
