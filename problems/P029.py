from typing import Set


def ans():
    arr: Set[int] = set()
    max_power: int = 100
    # for all bases
    for a in range(2, max_power + 1):
        # calculate powers
        p: int = a * a
        for b in range(2, max_power + 1):
            arr.add(p)
            p *= a
    return len(arr)
