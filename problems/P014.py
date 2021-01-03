from typing import Dict, List


def ans():
    chain_length: Dict[int] = dict()
    chain_length[1] = 1
    for i in range(2, 10 ** 6):
        cur_chain: List[int] = []
        j = i
        while j not in chain_length:
            cur_chain.append(j)
            j = next_collatz(j)
        # now it is in chain_length dict for the first time in the chain, and j is not in the cur_chain list
        plus_length = 1
        j_chain_length = chain_length[j]
        for k in reversed(cur_chain):
            chain_length[k] = j_chain_length + plus_length
            plus_length += 1
    return max(chain_length, key=lambda t: chain_length[t])


def next_collatz(x: int):
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1
