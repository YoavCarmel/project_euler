from sympy import isprime, nextprime


def ans():
    can = set()
    num = 3

    def try_find(n):
        p = 3
        if n in can:
            return True
        if isprime(n):
            can.add(n)
            return True
        while p < n:
            s = 1
            while (p + 2 * s * s) < n:
                can.add(p + 2 * s * s)
                s += 1
            if (p + 2 * s * s) == n:
                can.add(n)
                return True
            p = nextprime(p)
        return False

    while True:
        if num not in can:
            if not try_find(num):
                return num
        num += 2
