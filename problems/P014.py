from typing import Dict, List


def ans():
    chain_length: Dict[int] = dict()
    chain_length[1] = 1
    for i in range(2, 10 ** 6):
        calculate_chain_length(i, chain_length)
    return max(chain_length, key=lambda t: chain_length[t])


def next_collatz(x: int) -> int:
    """
    calculate the next number of the chain
    :param x: the current number
    :return: the next number
    """
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1


def calculate_chain_length(x: int, chain_length: Dict[int, int]) -> int:
    """
    calculate the length of the whole chain and update the chain_length dict
    :param chain_length: known chains lengths
    :param x: number to get length of its chain
    :return: the length of the chain
    """
    if x in chain_length:
        return chain_length[x]
    curr_chain: List[int] = []
    while x not in chain_length:
        curr_chain.append(x)
        x = next_collatz(x)
    # now it is in chain_length dict for the first time in the chain, and x is not in the curr_chain list.
    # add all numbers in the chain to the dict
    plus_length: int = 1
    x_chain_length: int = chain_length[x]
    for k in reversed(curr_chain):
        chain_length[k] = x_chain_length + plus_length
        plus_length += 1
