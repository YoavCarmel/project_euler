def ans():
    p: float = 1
    for den in range(1, 100):
        if den % 10 == 0:
            continue
        for num in range(1, den):
            # remove the trivial solution of nn/dd = n/d, and check if they match
            if not (den % 11 == 0 and num % 11 == 0) and \
                    num / den == (num // 10) / (den % 10) and num % 10 == den // 10:
                p *= den / num
    return int(p)
