def ans():
    n = 50
    return sum([rec(n,m,dict())-1 for m in [2,3,4]])


def rec(length_left, m, values):
    if length_left < m:
        return 1  # finished an option
    # in each step, choose between one more grey, or a new red with any length from 3 to the end
    s = 0
    # one more grey
    if length_left - 1 in values:
        s += values[length_left - 1]
    else:
        res = rec(length_left - 1, m, values)
        values[length_left - 1] = res
        s += res
    # one more tile of size m
    if length_left - m in values:
        s += values[length_left - m]
    else:
        res = rec(length_left - m, m, values)
        values[length_left - m] = res
        s += res
    return s


"""
def rec(length_left, values):
    if length_left < 3:
        return 1  # finished an option
    # in each step, choose between one more grey, or a new red with any length from 3 to the end
    s = 0
    # one more grey
    if length_left - 1 in values:
        s += values[length_left - 1]
    else:
        res = rec(length_left - 1, values)
        values[length_left - 1] = res
        s += res
    # red with any length that does not end at the end
    for i in range(3, length_left):
        # minus 1 for the grey between this and the next
        if length_left - i - 1 in values:
            s += values[length_left - i - 1]
        else:
            res = rec(length_left - i - 1, values)
            values[length_left - i - 1] = res
            s += res
    s += 1  # red that ends at the end
    return s
"""
