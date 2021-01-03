from objects.frac import Frac
from libs.numbers_properties import digits_sum


def ans():
    generated_list = generate_list(100)
    generated_list.reverse()
    f = Frac(generated_list[0], 1)
    for i in generated_list[1:]:
        f = Frac(i, 1) + f.flip()
    n = f.simplify().n
    return digits_sum(n)


def generate_list(n):
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
