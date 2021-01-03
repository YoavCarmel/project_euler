def ans():
    num = 1
    s = num
    square_size = 1001
    for size in range(3, square_size + 1, 2):
        h = size - 1
        for i in range(4):
            num += h
            s += num
    return s
