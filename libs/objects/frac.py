from math import gcd, inf


class Frac:
    def __init__(self, n, d=1, reduce=True):
        if d == 0:
            raise Exception("division by 0")
        if reduce:
            n, d = Frac.reduce_frac(n, d)
        self.n: int = n
        self.d: int = d
        self.is_int = self.d == 1
        self.hash_val = self.calc_hash()

    def calc_hash(self):
        return hash(self.n) ^ hash(self.d)

    def simplify(self):
        n, d = Frac.reduce_frac(self.n, self.d)
        return Frac(n, d, reduce=False)

    @staticmethod
    def reduce_frac(n, d) -> (int, int):
        if d == 1:
            return n, d
        g = gcd(n, d)
        if d < 0:
            return -n // g, -d // g
        else:
            return n // g, d // g

    def __add__(self, other):
        if isinstance(other, Frac):
            return Frac(self.n * other.d + self.d * other.n, self.d * other.d)
        if isinstance(other, int):
            if self.is_int:
                return Frac(other + self.n, reduce=False)
            else:
                return self + Frac(other, reduce=False)
        if other == inf or other == -inf:
            return other
        else:
            raise NotImplemented()

    def __mul__(self, other):
        if isinstance(other, Frac):
            return Frac(self.n * other.n, self.d * other.d)
        if isinstance(other, int):
            if self.is_int:
                return Frac(other * self.n, reduce=False)
            else:
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
        return Frac(-self.n, self.d, reduce=False)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return self - other

    def __int__(self):
        return self.n // self.d

    def __float__(self):
        return self.n / self.d

    def __truediv__(self, other):
        if isinstance(other, Frac):
            return Frac(self.n * other.d, self.d * other.n)
        if isinstance(other, int):
            return Frac(self.n, self.d * other)
        else:
            raise NotImplemented()

    def flip(self):
        return Frac(self.d, self.n, reduce=False)

    def __hash__(self):
        return self.hash_val

    def __ge__(self, other):
        if isinstance(other, int):
            return self.n // self.d >= other
        if isinstance(other, Frac):
            return self.n * other.d >= self.d * other.n
        if isinstance(other, float):
            if other == inf:
                return False
            if other == -inf:
                return True
            return other <= float(self)
        else:
            raise NotImplemented()

    def __eq__(self, other):
        if isinstance(other, Frac):
            return self.n == other.n and self.d == other.d
        if isinstance(other, float):
            if other == inf:
                return self.d == 0 and self.n > 0
            if other == -inf:
                return self.d == 0 and self.n < 0
            return other == float(self)
        if isinstance(other, int):
            if not self.is_int:
                return False
            return self.n == other
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
