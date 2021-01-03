from math import sqrt


def ans():
    max_L = 1.5 * 10 ** 6
    solutions = dict()
    s = 1
    while s < (sqrt(1 + 2 * max_L) - 1) / 2 + 1:
        for t in range(1, s):
            L = 2 * s * s + 2 * s * t
            if L > max_L:
                break
            if L not in solutions.keys():
                solutions[L] = set()
            solutions[L].add(tuple(sorted([2 * s * t, s * s - t * t])))
        s += 1
    for i in sorted(solutions.keys()):
        for k in range(2, int(max_L / i) + 1):
            if i * k not in solutions.keys():
                solutions[i * k] = set()
            for t in solutions[i]:
                solutions[i * k].add(tuple(sorted([t[0] * k, t[1] * k])))
    count = 0
    for i in solutions.keys():
        if len(solutions[i]) == 1:
            count += 1
    return count

