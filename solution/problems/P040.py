def ans():
    s = ""
    size = 10 ** 6
    for i in range(1, size):
        s += str(i)
    p = 1
    for i in range(6 + 1):
        p *= int(s[10 ** i - 1])
    return p
