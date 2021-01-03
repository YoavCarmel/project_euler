from math import sqrt

"""
using calculus, the min distance for a,b,c if sqrt(a^2+(b-c)^2)
but we should also choose which of them is the a
because a>=b>=c, it is better to put a outside so the squares are more balanced
"""


def ans():
    count = 0
    M = 0
    while count < 10 ** 6:
        M += 1
        a = M
        for bc in range(2, 2 * a + 1):
            x = sqrt(bc ** 2 + a ** 2)
            if x.is_integer():
                count += int(bc / 2) - max(bc - a - 1, 0)  # add all pairs (b,c) such that b+c=bs, a>=b>=c>=1
    return M
