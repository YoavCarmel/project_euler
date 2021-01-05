from math import factorial
from typing import Dict, List, Set


def ans():
    factorial_dict: Dict[int, int] = {i: factorial(i) for i in range(10)}
    chain_length_dict: Dict[int, int] = dict()
    max_i = 10 ** 6
    for i in range(max_i + 1):
        # calculate chain
        chain: List[int] = list()
        chain_set: Set[int] = set()
        j = i
        # continue until we get a number we know or we get stuck in a loop
        while j not in chain_set and j not in chain_length_dict:
            chain.append(j)
            chain_set.add(j)
            j = fact_digits(j, factorial_dict)
        # if got a number we know
        if j in chain_length_dict:
            plus_s = 1
            for k in reversed(chain):
                chain_length_dict[k] = chain_length_dict[j] + plus_s
                plus_s += 1
        else:  # got a loop
            loop_start = chain.index(j)
            for k in range(loop_start):
                chain_length_dict[chain[k]] = len(chain) - k
            for k in range(loop_start, len(chain)):
                chain_length_dict[chain[k]] = len(chain) - loop_start
    return len([i for i in chain_length_dict if chain_length_dict[i] == 60])


def fact_digits(n, factorial_dict):
    """
    :param n: input number
    :param factorial_dict: known factorials of digits
    :return: sum of factorial of digits
    """
    s = 0
    while n > 0:
        s += factorial_dict[n % 10]
        n //= 10
    return s
