def ans():
    n = 100
    # a[i][j] is number of partitions with sum i and biggest number is j, and j must be there
    a = [[0] * (n + 1)]
    for i in range(n):
        a.append([0, 1] + [0] * (n - 1))
    for i in range(1, n + 1):
        for j in range(2, i):
            a[i][j] = sum(a[i - j][:j + 1])
        a[i][i] = 1
        for j in range(i + 1, n):
            a[i][j] = 0
    return sum(a[-1]) - 1
