def ans():
    n: int = 1000-1
    return as_sum(3, 3, n // 3) + as_sum(5, 5, n // 5) - as_sum(15, 15, n // 15)


def as_sum(a1, d, n):
    return (2 * a1 + (n - 1) * d) * n // 2
