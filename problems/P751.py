from decimal import *
from typing import List


def ans():
    base = 5 * 10 ** 24
    p = base
    for i in range(1, 100):
        d = Decimal(f"2.{p}")
        seq = get_seq(d, 24)
        seq_dec = seq_concat(seq, rounding=24)
        # binary search the wanted theta
        if seq_dec > d:
            p += base // (2 ** i)
        elif seq_dec < d:
            p -= base // (2 ** i)
        else:
            break
    return d


def get_seq(theta: Decimal, max_n=10) -> List[int]:
    bn = theta
    seq: List[int] = list()
    for n in range(1, max_n + 1):
        an = int(bn)
        seq.append(an)
        bn = int(bn) * (bn - int(bn) + 1)
    return seq


def seq_concat(seq: List[int], rounding=None):
    s = "".join(str(i) for i in seq)
    s = s[0] + "." + s[1:]
    if rounding is not None:
        s = s[:2 + rounding]
    return Decimal(s)
