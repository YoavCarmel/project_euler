def ans():
    num: int = 1
    s: int = num
    square_size: int = 1001
    # for layer in spiral
    for size in range(3, square_size + 1, 2):
        h = size - 1
        # for value in layer
        for i in range(4):
            num += h
            s += num
    return s
