from typing import List

from objects.frac import Frac
from libs.numbers_properties import digits_sum


def ans():
    generated_list: List[int] = generate_list(100)
    generated_list.reverse()
    f: Frac = Frac(generated_list[0])
    for i in generated_list[1:]:
        f = Frac(i) + f.flip()
    n = f.simplify().n
    return digits_sum(n)


def generate_list(n: int) -> List[int]:
    """
    generate the list by the pattern we found
    :param n: number of elements in the output list
    :return: the generated list
    """
    if n == 1:
        return [2]
    if n == 2:
        return [2, 1]
    if n == 3:
        return [2, 1, 2]
    k = 2
    result = [2, 1, 2]
    for i in range(int(n / 3) + 2):
        result += [1, 1, 2 * k]
        k += 1
    return result[:n]
