from itertools import permutations


def ans():
    n = 10
    l = list(range(1, n + 1))
    p = list(permutations(l))
    magic = set()
    for i in p:
        if handle_perm(i) is not None:
            magic.add(handle_perm(i))
    l = list()
    for i in magic:
        l.append(magic_to_string(i))
    l.sort()
    for i in range(len(l)):
        if len(l[i]) == 17:
            return l[i - 1]
    return max(l)


def handle_perm(l):
    # split to outer half and inner half
    o = l[:len(l) // 2]
    i = l[len(l) // 2:]
    #10 must be outside, because the request is for only 16 digit result, not 17
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
