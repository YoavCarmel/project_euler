from math import gcd, inf


class Frac:
    def __init__(self, n, d=1):
        if d == 0:
            raise Exception("division by 0")
        n, d = Frac.reduce_frac(n, d)
        self.n = n
        self.d = d

    def simplify(self):
        n, d = Frac.reduce_frac(self.n, self.d)
        return Frac(n, d)

    @staticmethod
    def reduce_frac(n, d) -> (int, int):
        g = gcd(n, d)
        if d < 0:
            return -n // g, -d // g
        else:
            return n // g, d // g

    def __add__(self, other):
        if type(other) is Frac:
            return Frac(self.n * other.d + self.d * other.n, self.d * other.d)
        if type(other) is int:
            return self + Frac(other, 1)
        if other == inf or other == -inf:
            return other
        else:
            raise NotImplemented()

    def __mul__(self, other):
        if type(other) is Frac:
            return Frac(self.n * other.n, self.d * other.d)
        if type(other) is int:
            return self * Frac(other)
        if other == inf or other == -inf:
            return other
        else:
            raise NotImplemented()

    def __str__(self):
        return str(self.n) + "/" + str(self.d)

    def __repr__(self):
        return str(self.n) + "/" + str(self.d)

    def __neg__(self):
        return Frac(-self.n, self.d)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return self - other

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
            return self >= other >= self
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
