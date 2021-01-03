def ans():
    limit = 100
    return sum([i for i in range(limit + 1)]) ** 2 - sum([i ** 2 for i in range(limit + 1)])
