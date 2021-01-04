def ans():
    s: str = ""
    size: int = 10 ** 6 // 5  # optimized for max length 10**6
    for i in range(1, size):
        s += str(i)
    p: int = 1
    for i in range(6 + 1):
        p *= int(s[10 ** i - 1])
    return p
