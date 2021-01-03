from tqdm import trange

from solution.libs.continued_fraction import rep_square


def ans():
    count = 0
    for i in trange(10001):
        if len(rep_square(i)) % 2 == 1:
            count += 1
    return count


