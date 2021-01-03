def ans():
    m = 1000000007
    last_fib = 90
    f = fib_list(last_fib)
    su = 0
    for i in f[2:]:
        su += best_s_sum(i, m)
    return su % m


def best_s_sum(n, m):
    return s_sum7(n, m)


"""
def s_sum1(n, mod):
    su = 0
    for i in range(n + 1):
        su += s(i) % mod
    return su % mod


def s_sum2(n, mod):
    su = 0
    res_str = "1"
    for i in range(1, n + 1):
        su += int(res_str) % mod
        if res_str[0] == '9':
            res_str = "1" + res_str
        else:
            res_str = str(int(res_str[0]) + 1) + res_str[1:]
    return su % mod


def s_sum3(n, mod):
    su = 0
    res_int = 1
    res_pow = 1
    for i in range(1, n + 1):
        su += res_int % mod
        if res_int // res_pow == 9:
            res_pow *= 10
        res_int += res_pow
    return su % mod


def s_sum4(n, mod):
    s1to9 = 45
    su = 0
    p = 1
    for i in range(n // 9):
        su += (s1to9 * p + 9 * (p - 1)) % mod
        p *= 10
    for i in range(9 * (n // 9) + 1, n + 1):
        su += s(i) % mod
    return su % mod


def s_sum5(n, mod):
    s1to9 = 45
    p = 10 ** (n // 9)
    su = (9 * ((p - 1) // 9) - 9 * (n // 9) + (s1to9 * (p // 9))) % mod
    for i in range(9 * (n // 9) + 1, n + 1):
        su += s(i) % mod
    return su % mod


def s_sum6(n, mod):
    s1to9 = 45
    p = 10 ** (n // 9)
    r = n % 9
    return ((p - 1)
            - 9 * (n // 9)
            + s1to9 * (p // 9)
            + r * (p - 1)
            + p * (r + 1) * r // 2) % mod
"""


def s_sum7(n, mod):
    s1to9 = 45
    p = pow(10, (n // 9), mod * 9)
    r = n % 9
    return ((p - 1)
            - 9 * (n // 9)
            + s1to9 * (p // 9)
            + r * (p - 1)
            + p * (r + 1) * r // 2) % mod


def fib_list(n):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    else:
        result = [0, 1]
        for i in range(1, n):
            result.append(result[-1] + result[-2])
        return result
