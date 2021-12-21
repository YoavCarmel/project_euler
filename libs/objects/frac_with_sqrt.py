from __future__ import annotations

from dataclasses import dataclass
from math import sqrt

from libs.objects.frac import Frac


@dataclass(init=True, repr=True)
class QPair:
    """
    data class that contains the whole part of the FracWithSqrt and the non-int part of the FracWithSqrt
    """
    whole: int
    rem: FracWithSqrt

    def __hash__(self):
        return hash(self.whole) ^ hash(self.rem)


class FracWithSqrt:
    """
    represents a value of rest + sqrt(inside) * coef, e.g. (1/4)+sqrt(7)*(2/3)
    """

    def __init__(self, sqrt_coef: Frac, rest: Frac, sqrt_inside):
        self.sqrt_coef: Frac = sqrt_coef  # coefficient of the sqrt term
        self.rest: Frac = rest  # fraction without sqrt coefficient
        self.sqrt_inside: int = sqrt_inside  # the inside of the sqrt

    def flip(self) -> FracWithSqrt:
        """
        :return: complex fraction that has value of 1/self
        """
        # should get 1/com_frac
        # 1/(a*sqrt(s)+b)=(a*sqrt(s)-b)/(a^2*s-b^2)
        a: Frac = self.sqrt_coef
        s: int = self.sqrt_inside
        b: Frac = self.rest
        den: Frac = (a * a * s) - (b * b)
        return FracWithSqrt(a / den, (-b) / den, s)

    def remainder(self) -> FracWithSqrt:
        """
        calculates the non-integer part as an object,
        calculate the non-sqrt-related number to subtract from self to get a number between 0 to 1
        :return: the non-integer part as an object
        """
        a: Frac = self.sqrt_coef
        s: int = self.sqrt_inside
        b: Frac = self.rest
        return FracWithSqrt(a, Frac(b.n - int(self) * b.d, b.d), s)

    def split_int_nonint(self) -> QPair:
        return QPair(int(self), self.remainder())

    def __repr__(self):
        return self.rest.__repr__() + " + sqrt(" + str(self.sqrt_inside) + ") * " + self.sqrt_coef.__repr__()

    def __eq__(self, other):
        return float(self) == float(other)

    def __hash__(self):
        return hash(self.rest) + hash(self.sqrt_coef) + hash(self.sqrt_inside)

    def __float__(self):
        return float(self.sqrt_coef) * sqrt(float(self.sqrt_inside)) + float(self.rest)

    def __int__(self):
        return int(float(self))
