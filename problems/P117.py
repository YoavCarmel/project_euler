def ans():
    n = 50
    return rec(n, dict())


def rec(length_left, values):
    if length_left < 2:
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
    # one more tile of size m
    for m in range(2, min(4+1, length_left+1)):
        if length_left - m in values:
            s += values[length_left - m]
        else:
            res = rec(length_left - m, values)
            values[length_left - m] = res
            s += res
    return s
