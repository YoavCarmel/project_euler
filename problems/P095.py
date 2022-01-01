from typing import Set

from libs.calculations.divisors import divisors_sum


def ans():
    max_chain = []
    million = 10 ** 6
    divs_sums = divisors_sum(million + 1, including_itself=False)  # this gives a massive improvement
    checked: Set[int] = set()
    for i in range(1, million + 1):
        # if we already saw i, dont calculate again
        if i in checked:
            continue
        chain_s = set()
        chain_l = list()
        s = i
        # continue as long as the chain does not exceed a million, and we do not get a number we have already seen
        while s <= million and s not in chain_s and s not in checked:
            checked.add(s)
            chain_s.add(s)
            chain_l.append(s)
            # move to the next
            s = divs_sums[s]
        if s > million:  # the reason for break was exceeding million, invalid chain
            continue
        if s in checked and s not in chain_s:  # the reason for break was not arriving a loop
            continue
        # add the last number as it was not added in the loop
        checked.add(s)
        # check if this is the longest until now
        length = len(chain_l) - chain_l.index(s)
        if length > len(max_chain):
            max_chain = chain_l[chain_l.index(s):]
    return min(max_chain)
