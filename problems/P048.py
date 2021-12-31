def ans():
    s: int = 0
    limit: int = 1000
    ten_ten: int = 10 ** 10
    for i in range(1, limit + 1):
        s += pow(i, i, ten_ten)  # pow modulo
    return s % ten_ten
