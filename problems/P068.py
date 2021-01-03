from itertools import permutations


def ans():
    n = 10
    n_range = list(range(1, n + 1))
    p = list(permutations(n_range))
    magic = set()
    for i in p:
        if handle_perm(i) is not None:
            magic.add(handle_perm(i))
    magic_strings = list()
    for i in magic:
        magic_strings.append(magic_to_string(i))
    magic_strings.sort()
    for i in range(len(magic_strings)):
        if len(magic_strings[i]) == 17:
            return magic_strings[i - 1]
    return max(magic_strings)


def handle_perm(perm):
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


def is_magic(lines):
    s = sum(lines[0])
    for i in lines[1:]:
        if s != sum(i):
            return False
    return True


def magic_to_string(lines):
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
