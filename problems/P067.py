def ans():
    p = load_pyramid()
    p.reverse()
    maxes = [p[0]]
    for i in range(1, len(p)):
        maxes.append([])
        for j in range(len(p[i])):
            maxes[i].append(p[i][j] + max(maxes[i - 1][j], maxes[i - 1][j + 1]))
    return maxes[-1][0]


def load_pyramid():
    f = open("files//P067.txt")
    p = []
    for line in f.readlines():
        p.append([int(i) for i in line.strip("\n").split(" ")])
    return p
