def ans():
    arr = set()
    max_power = 100
    for a in range(2, max_power + 1):
        for b in range(2, max_power + 1):
            arr.add(a ** b)
    return len(arr)
