from itertools import combinations


def ans():
    count = 0
    z_to_9 = set([i for i in range(10)])
    for i in combinations(z_to_9, 6):
        for j in combinations(z_to_9, 6):
            if is_good_arrangement(set(i), set(j)):
                count += 1
    return count // 2  # it counts twice for each arrangement, ine for each side


def is_good_arrangement(c1, c2):  # 01, 04, 09, 16, 25, 36, 49, 64, 81
    # 01:
    if not ((0 in c1 and 1 in c2) or (0 in c2 and 1 in c1)):
        return False
    # 04:
    if not ((0 in c1 and 4 in c2) or (0 in c2 and 4 in c1)):
        return False
    # 09:
    if not ((0 in c1 and 9 in c2) or (0 in c2 and 9 in c1) or (0 in c1 and 6 in c2) or (0 in c2 and 6 in c1)):
        return False
    # 16
    if not ((1 in c1 and 6 in c2) or (1 in c2 and 6 in c1) or (1 in c1 and 9 in c2) or (1 in c2 and 9 in c1)):
        return False
    # 25
    if not ((2 in c1 and 5 in c2) or (2 in c2 and 5 in c1)):
        return False
    # 36
    if not ((3 in c1 and 6 in c2) or (3 in c2 and 6 in c1) or (3 in c1 and 9 in c2) or (3 in c2 and 9 in c1)):
        return False
    # 49 and 64
    if not ((4 in c1 and 6 in c2) or (4 in c2 and 6 in c1) or (4 in c1 and 9 in c2) or (4 in c2 and 9 in c1)):
        return False
    # 81:
    if not ((8 in c1 and 1 in c2) or (8 in c2 and 1 in c1)):
        return False
    return True
