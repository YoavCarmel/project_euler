from itertools import permutations

from libs.types_converting import list_to_num


def ans():
    return list_to_num(list(list(permutations([i for i in range(10)]))[10 ** 6 - 1]))
