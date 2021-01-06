from itertools import permutations
from typing import FrozenSet, Set, Tuple, List


def ans():
    magic: Set[FrozenSet[Tuple[int, int, int]]] = set()
    # get all permutations, find valid n-gons
    for i in permutations(range(1, 10 + 1)):
        if handle_perm(i) is not None:
            magic.add(handle_perm(i))
    # get the strings of the valid
    magic_strings: List[str] = [magic_to_string(i) for i in magic]
    magic_strings = [s for s in magic_strings if len(s) == 16]
    return max(magic_strings)


def handle_perm(perm: Tuple[int, ...]):
    """
    :param perm: a permutations
    :return: frozenset of the lines of the valid n-gon, None if not valid
    """
    # split to outer half and inner half
    o = perm[:len(perm) // 2]
    i = perm[len(perm) // 2:]
    # 10 must be outside, because the request is for only 16 digit result, not 17
    if 10 in i:
        return None
    # now calc each line in the shape
    lines = [(o[k], i[k], i[(k + 1) % len(i)]) for k in range(len(i))]
    if is_magic(lines):
        return frozenset(lines)
    return None


def is_magic(lines: List[Tuple[int, ...]]):
    """
    :param lines: a list of lines
    :return: True if all lines have the same sum
    """
    s = sum(lines[0])
    for i in lines[1:]:
        if s != sum(i):
            return False
    return True


def magic_to_string(lines: FrozenSet[Tuple[int, ...]]) -> str:
    """
    :param lines: lines of valid n-gon
    :return: string representations
    """
    s = ""
    m = min(lines)
    lines = set(lines)
    while len(lines) != 0:
        for i in m:
            s += str(i)
        lines.remove(m)
        for k in lines:
            if k[1] == m[2]:
                m = k
                break
    return s
