from typing import List


def ans():
    p: List[List[int]] = load_pyramid()
    p.reverse()
    maxes: List[List[int]] = [p[0]]
    # use dynamic programming to keep the maxes of the prev layers
    for i in range(1, len(p)):
        maxes.append([])
        for j in range(len(p[i])):
            maxes[i].append(p[i][j] + max(maxes[i - 1][j], maxes[i - 1][j + 1]))
    return maxes[-1][0]


def load_pyramid() -> List[List[int]]:
    f = open("files//P067.txt")
    p: List[List[int]] = []
    for line in f.readlines():
        p.append([int(i) for i in line.strip("\n").split(" ")])
    return p
