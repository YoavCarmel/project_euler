from collections import Iterable
from itertools import combinations, chain


def power_set(iterable: Iterable, with_empty: bool = True) -> Iterable:
    """
    returns the power set of the input iterable
    :param iterable: the iterable to create its power set
    :param with_empty: include/exclude the empty set
    :return: the power set, as iterable
    """
    s = list(iterable)
    # formula form the internet
    res = chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))
    if not with_empty:
        next(res, None)
    return res
