from math import gcd, inf


class Frac:
    def __init__(self, n, d):
        g = gcd(n, d)
        self.n = n // g
        self.d = d // g

    def simplify(self):
        g = gcd(self.n, self.d)
        return Frac(self.n // g, self.d // g)

    def __add__(self, other):
        if type(other) is int:
            return self + Frac(other, 1)
        if type(other) is Frac:
            return Frac(self.n * other.d + self.d * other.n, self.d * other.d).simplify()
        else:
            raise NotImplemented()

    def __mul__(self, other):
        if type(other) is int:
            return self * Frac(other, 1)
        if type(other) is Frac:
            return Frac(self.n * other.n, self.d * other.d).simplify()
        else:
            print(other)
            raise NotImplemented()

    def __str__(self):
        return str(self.n) + "/" + str(self.d)

    def __neg__(self):
        return Frac(-self.n, self.d)

    def __sub__(self, other):
        return self + (-other)

    def __int__(self):
        return self.n // self.d

    def __float__(self):
        return self.n / self.d

    def flip(self):
        return Frac(self.d, self.n)

    def __truediv__(self, other):
        if type(other) is int:
            return self * Frac(1, other)
        if type(other) is Frac:
            return self * other.flip()
        else:
            raise NotImplemented()

    def __hash__(self):
        return hash(self.n) + hash(self.d)

    def __ge__(self, other):
        if type(other) is int or type(other) is float:
            if other == inf:
                return False
            if other == -inf:
                return True
            return other <= float(self)
        if type(other) is Frac:
            return self.n * other.d >= self.d * other.n
        else:
            raise NotImplemented()

    def __eq__(self, other):
        if type(other) is int or type(other) is float:
            if other == inf:
                return self.d == 0 and self.n > 0
            if other == -inf:
                return self.d == 0 and self.n < 0
            return other == float(self)
        if type(other) is Frac:
            return self >= other and other >= self
        else:
            raise NotImplemented()

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self >= other and self != other

    def __le__(self, other):
        return not self > other

    def __lt__(self, other):
        return not self >= other
