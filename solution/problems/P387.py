from typing import Set, Dict
from collections import defaultdict

from sympy import isprime
from solution.libs.numbers_properties import digits_sum


def ans():
    n = 14
    """
    we want to generate the numbers going up.
    we know that for each of these primes, when removing the last digit we get 
    a strong, right-truncatable Harshad number.
    to get a right-truncatable Harshad number the attribute should hold for all prefixes of the number,
    so we can build it iteratively and get the only right-truncatable Harshad numbers if each number of digits.
    """
    rt_harshad_by_digs: Dict[int, Set[int]] = defaultdict(
        set)  # number of digits->rt_harshad_by_digs of this number of digits
    rt_harshad_by_digs[1] = {i for i in range(1, 10)}
    for number_of_digs in range(2, n):  # excluding n because we add another digit at the end
        for num in rt_harshad_by_digs[number_of_digs - 1]:
            digs_sum = digits_sum(num)
            num10 = num * 10
            for new_dig in range(10):
                if (num10 + new_dig) % (digs_sum + new_dig) == 0:
                    rt_harshad_by_digs[number_of_digs].add(num10 + new_dig)
    # now get a set of all of them
    rt_harshad: Set[int] = set()
    for k, s in rt_harshad_by_digs.items():
        rt_harshad = rt_harshad.union(s)
    # we want to add only the strong, right-truncatable Harshad numbers
    srt_harshad = {i for i in rt_harshad if isprime(i // digits_sum(i))}
    # now we want to get the set of all primes that after removing the right digit we get a number of this list
    srt_harshad_primes = {i * 10 + d for i in srt_harshad for d in [1, 3, 7, 9] if isprime(i * 10 + d)}
    return sum(srt_harshad_primes)
