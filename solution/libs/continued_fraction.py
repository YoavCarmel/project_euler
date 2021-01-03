from math import sqrt
from typing import NamedTuple
from solution.objects.frac import Frac


class ComplexFrac(NamedTuple):
    sqrt_coef: Frac
    rest: Frac
    sqrt_inside: int


class QPair(NamedTuple):
    whole: int
    rem: ComplexFrac


def rep_square(x):  # calc for sqrt(x)
    sqrt_x = sqrt(x)
    if sqrt_x.is_integer():
        return []
    s = set()  # set of all pairs of (a_i, rest)
    l = list()  # list of these pairs
    pair = QPair(int(sqrt_x), ComplexFrac(Frac(1, 1), Frac(-int(sqrt_x), 1), x))
    while pair not in s:
        s.add(pair)
        l.append(pair)
        # get new pair
        r = __flip_complex_frac(pair.rem)
        r_value = __com_frac_value(r)
        pair = QPair(int(r_value), __calc_rem(r))
    return [i.whole for i in l[l.index(pair):]]


def __flip_complex_frac(com_frac):  # com_frac is a complex_frac type
    # should get 1/com_frac
    # 1/(as+b)=(as-b)/((as)^2-b^2)
    a = com_frac.sqrt_coef
    s = com_frac.sqrt_inside
    b = com_frac.rest
    den = (a * a * s) - (b * b)  # s=sqrt^2
    return ComplexFrac(a / den, (-b) / den, s)


def __calc_rem(com_frac):
    a = com_frac.sqrt_coef
    s = com_frac.sqrt_inside
    b = com_frac.rest
    return ComplexFrac(a, Frac(b.n - int(__com_frac_value(com_frac)) * b.d, b.d), s)


def __com_frac_value(r):
    return float(r.sqrt_coef) * sqrt(float(r.sqrt_inside)) + float(r.rest)
