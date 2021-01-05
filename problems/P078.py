from typing import Dict

from sympy import divisors


def ans():
    print("takes about 4 minutes")
    # p(n)=1/n* (sum from k=0 to n-1 of p(k)*dv_sum(n-k))
    dv_sum: Dict[int] = dict()
    p: Dict[int] = dict()
    p[0] = 1
    n = 1
    thresh = 10 ** 6
    while True:
        print(n)
        dv_sum[n] = sum(divisors(n))
        s = 0
        for k in range(0, n):
            s += dv_sum[n - k] * p[k]
        s //= n
        if s % thresh == 0:
            return n
        p[n] = s
        n += 1

# too slow
# def ans():
#     thresh = 10 ** 6
#     # a[i][j] is number of partitions with sum i and biggest number is j
#     a: Dict[int, Dict[int, int]] = defaultdict(dict)
#     a[0][0] = 1
#     i = 1
#     while True:
#         print(i)
#         a[i][0] = 0
#         for j in range(1, i + 1):
#             # either put j and handle the rest, or dont put j and lower it by 1
#             a[i][j] = a[i - j][min(i - j, j)] + a[i][j - 1]
#         if i>1 and (a[i][i]-1)%thresh==0:
#             return i
#         i += 1
