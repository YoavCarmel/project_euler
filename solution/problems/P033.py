def ans():
    p = 1
    for down in range(1, 100):
        for up in range(1, down):
            if not (down % 11 == 0 and up % 11 == 0) and down % 10 != 0:
                if up / down == (up // 10) / (down % 10) and up % 10 == down // 10:
                    p *= down/up
    return int(p)
