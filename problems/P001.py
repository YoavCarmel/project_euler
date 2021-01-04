def ans():
    s: int = 0
    n: int = 1000
    for i in range(n):
        # if i is divisible by 3 or 5, add it to the sum
        if i % 3 == 0 or i % 5 == 0:
            s += i
    return s
