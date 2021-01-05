from objects.frac import Frac


def ans():
    max_d = 10 ** 6
    best_frac = Frac(0)
    # get all fractions close to 3/7
    for i in range(1, max_d + 1):
        if i % 7 == 0:
            continue
        fi = Frac((3 * i) // 7, i)
        if best_frac < fi:  # and they are for sure smaller than 3/7
            best_frac = fi
    return best_frac.n
