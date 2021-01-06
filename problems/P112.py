from typing import List

from libs.types_converting import num_to_list


def ans():
    percent = 99
    bouncy_count = 0
    i = 1
    while True:
        if is_bouncy(i):
            bouncy_count += 1
        if bouncy_count / i == percent / 100:
            return i
        i += 1


def is_bouncy(x: int) -> bool:
    """
    :param x: input number
    :return: True if the number is bouncy
    """
    digs: List[int] = num_to_list(x)
    form = 0
    for i in range(len(digs) - 1):
        if form == 0:
            if digs[i] > digs[i + 1]:
                form = -1
            elif digs[i] < digs[i + 1]:
                form = 1
        else:
            if digs[i] > digs[i + 1] and form == 1:
                return True
            if digs[i] < digs[i + 1] and form == -1:
                return True
    return False
