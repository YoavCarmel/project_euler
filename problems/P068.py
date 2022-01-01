from itertools import permutations, combinations, product
from typing import FrozenSet, Set, Tuple, List


def ans():
    magic: Set[FrozenSet[Tuple[int, int, int]]] = set()
    all_nums = {i for i in range(1, 10 + 1)}
    # get all permutations, find valid n-gons
    for c in combinations(range(1, 10), 5):
        for inside, outside in product(permutations(c), permutations(all_nums - set(c))):
            hp = handle_perm(inside, outside)
            if hp is not None:
                magic.add(hp)
    # get the strings of the valid
    magic_strings: List[str] = [magic_to_string(i) for i in magic]
    return max(magic_strings)


def handle_perm(i: Tuple[int, ...], o: Tuple[int, ...]):
    """
    :param i: a permutation of the inside
    :param o: a permutation of the outside
    :return: frozenset of the lines of the valid n-gon, None if not valid
    """
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
