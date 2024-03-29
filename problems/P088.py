from collections import defaultdict, Counter
from itertools import combinations
from typing import Set, List, Tuple, Dict, NamedTuple, Any

from sympy import factorint


class Subgroup(NamedTuple):
    group: Tuple[int]
    sum: int
    length: int


def ans():
    max_k = 12000
    k_set: Set[int] = set([i for i in range(2, max_k + 1)])  # all k values to find solution to
    k_results_n_solutions: Set[int] = set()  # the n values that are solutions to the k values
    n = 2
    while len(k_set) > 0:  # while there are still k values we did not find solution to
        n_ks: Set[int] = handle_n(n)  # find all the k solutions that are possible for the current n
        new_ks: Set[int] = n_ks.intersection(k_set).difference({1})  # get only the new k solutions that this n gives us
        if len(new_ks) != 0:  # if the current n gave us new solutions, add it to the n solutions set
            k_results_n_solutions.add(n)
            k_set = k_set.difference(new_ks)  # remove the new k solutions from the k values set
        n += 1  # go to the next n
    return sum(k_results_n_solutions)


def handle_n(n: int) -> Set[int]:
    """
    :param n: input number
    :return: a set of all k values that n gives us
    """
    k_sols: Set[int] = set()  # all the k values that n gives us
    l: List[Subgroup] = all_product_subgroups(n)
    for sg in l:
        """
        now take each subgroup. we know its product, it is n.
        we can add as many 1's as we want to the product without changing it.
        we will add the number of 1's we need to make the sum equal n too.
        then, out k is the length of the subgroup, plus the number of 1's we added,
        which is n minus the subgroup's sum
        """
        k = sg.length + n - sg.sum
        k_sols.add(k)
    return k_sols


def all_product_subgroups(n: int) -> List[Subgroup]:
    """
    :param n: input number
    :return: a list of all subgroups for the input number
    """
    pfl_dict: Dict[int, int] = factorint(n)
    pfl: List[int] = [i for i in pfl_dict for _ in range(pfl_dict[i])]  # get prime factors of n with repetition
    """
    dictionary that maps length of list to all Subgroup of this length, that can be made by taking the initial
    prime factors list and multiplying some og the numbers in it to decrease the length of the list
    """
    lengths: Dict[int, Set[Subgroup]] = defaultdict(set)
    """
    add the first pair in the dictionary, which is the initial prime factors list
    """
    lengths[len(pfl)] = {Subgroup(tuple(pfl), sum(pfl), len(pfl))}
    """
    go over all lengths of lists, starting with the initial length and going to 2.
    in each iteration, build the next length's lists.
    """
    for t in range(len(pfl), 2, -1):
        lengths[t - 1] = get_next_length_subgroups(lengths[t], t - 1)
    return [sg for k in lengths for sg in lengths[k]]


def get_next_length_subgroups(lengths_t, next_t):
    """
    :param lengths_t: the previous length's subgroups
    :param next_t: the new length
    :return: a set of the subgroups of length next_t
    """
    res: Set[Subgroup] = set()
    """
    we will go over all pairs in the group, and for each pair, remove its values and add their product.
    if there is a number duplicated, it will do the same calculations over and over again on the same number,
    but each time for another instance of it.
    so in order to prevent it, we will only go over each number once, and take care of duplicated numbers,
    that the only additional thing we need to do is to add each number's product with itself.
    """
    for i in lengths_t:  # for each subgroup in the current length:
        i_duplicates: List[int] = get_duplicates_in_list(list(i.group))  # the duplicates list
        i_pfs: Set[int] = set(i.group)  # the unique values
        # now take care of our process of taking pairs of numbers and replacing them with their product
        for pair in combinations(i_pfs, 2):  # for each pair in the list
            # get the subgroup without the pair
            i_copy = list(i.group).copy()
            i_copy.remove(pair[0])
            i_copy.remove(pair[1])
            # add the pair's product
            i_copy.append(pair[0] * pair[1])
            # add the new subgroup, calculate the new sum in O(1) using given info
            res.add(Subgroup(tuple(sorted(i_copy)), i.sum - pair[0] - pair[1] + pair[0] * pair[1], next_t))
        for num in i_duplicates:
            # get the subgroup without the pair
            i_copy = list(i.group).copy()
            i_copy.remove(num)
            i_copy.remove(num)
            # add the pair's product
            i_copy.append(num * num)
            # add the new subgroup, calculate the new sum in O(1) using given info
            res.add(Subgroup(tuple(sorted(i_copy)), i.sum - 2 * num + num * num, next_t))
    return res


def get_duplicates_in_list(values: List[Any]) -> List[Any]:
    """
    :param values: a list of values
    :return: all values that appear more than once in the input list
    """
    counts = Counter(values)
    return [i for i in counts if counts[i] > 1]
