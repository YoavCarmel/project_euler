from sympy import divisors


def ans():
    print("takes about 4 minutes")
    # p(n)=1/n* (sum from k=0 to n-1 of p(k)*dv_sum(n-k))
    dv_sum = [None]
    p = [1]
    n = 1
    thresh = 10 ** 6
    while True:
        dv_sum.append(sum(divisors(n)))
        s = 0
        for k in range(0, n):
            s += dv_sum[n - k] * p[k]
        s //= n
        if s % thresh == 0:
            return n
        p.append(s)
        n += 1



