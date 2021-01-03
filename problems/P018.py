import random


def ans():
    p = load_pyramid()

    # print(maxLinesCalc(p))
    # print(brute(p,0,0))

    return brute(p, 0, 0)


def load_pyramid():
    p = [[75], [95, 64], [17, 47, 82], [18, 35, 87, 10], [20, 4, 82, 47, 65], [19, 1, 23, 75, 3, 34]]
    """
    p.append([88, 2, 77, 73, 7, 63, 67])
    p.append([99, 65, 4, 28, 6, 16, 70, 92])
    p.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
    p.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
    p.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
    p.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
    p.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
    p.append([63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
    p.append([4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23])
    """
    return p


def brute(p, line, place):
    if line == len(p) - 1:
        return p[line][place]
    # else, call both right and left
    return max(brute(p, line + 1, place), brute(p, line + 1, place + 1)) + p[line][place]


def create_pyramid(lines):
    p = []
    for i in range(lines):
        p.append([])
        for j in range(i + 1):
            p[i].append(random.randint(1, 99))
    return p
