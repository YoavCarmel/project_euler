from typing import List, Set, Union, NamedTuple
from solution.libs.special_groups import is_special_sum_set


class MinValueDepth(NamedTuple):
    values: List[int]
    sums: List[int]


class Solution(NamedTuple):
    solution_list: List[int]
    solution_sum: int


def ans():
    print("solution takes about 9 seconds")
    n = 7
    sol = solve(n)
    return "".join([str(i) for i in reversed(sol)])


def solve(max_depth: int) -> List[int]:
    """
    calculates for all lower depths before, to get the min starting value for each depth
    :param max_depth: the depth to return its answer
    :return: the result list of the input depth
    """
    min_value_depth = MinValueDepth([0, 1], [0, 1])
    for n in range(2, max_depth):
        res = calc(n, min_value_depth)
        min_value_depth.values.append(res[0])
        min_value_depth.sums.append(min_value_depth.sums[-1] + min_value_depth.values[n])
    return calc(max_depth, min_value_depth)


def calc(max_depth: int, min_value_depth: MinValueDepth) -> List[int]:
    """
    calculates the answer for given max depth. iterates on the first item of the answer,
    then calls rec for the rest of the solution. continues until certain that the found solution is min sum.
    :param max_depth: the depth to calculate
    :param min_value_depth: min values for previous depths
    :return: solution for input depth
    """
    # for depth=1
    i = min_value_depth.values[max_depth - 1] + 1
    # the current found solution
    best_found: Solution = None
    while True:
        # if we are sure that the current i cannot bring a better solution
        # because the current i with the min possible values (min solution of previous depth) is still too big
        if best_found is not None and i >= best_found.solution_sum - min_value_depth.sums[-1]:
            break
        # limit the sum of the next calculation to the sum of the best solution found
        max_sum_for_iter = None if best_found is None else best_found.solution_sum - i
        res = rec([i], {0, i}, max_depth, max_sum_for_iter, min_value_depth)
        # if we found a first solution, or a better solution
        if res is not None and (best_found is None or best_found.solution_sum > sum(res)):
            best_found = Solution(res, sum(res))
        i += 1
    return best_found.solution_list


# returns list of max_depth len he found to work
def rec(curr_nums: List[int], curr_subsets_sums: Set[int], max_depth: int, max_sum: Union[int, None],
        min_value_depth: MinValueDepth) -> List[int]:
    """
    calculate recursively the solution for the input depth with given first element
    :param curr_nums: the currently given list to complete
    :param curr_subsets_sums: the sums of all subsets of curr_nums
    :param max_depth: the length of the solution list
    :param max_sum: the max sum valid for a good solution
    :param min_value_depth: solutions of previous depths
    :return: solution for the input depth with given first element
    """
    curr_depth = len(curr_nums) + 1
    if curr_depth - 1 == max_depth:
        return curr_nums.copy()
    best_found = None
    last = curr_nums[-1]
    if max_sum is not None:
        last = min(last, max_sum - min_value_depth.sums[max_depth - curr_depth])
    # second smallest must be at least half of the biggest,
    i = max(min_value_depth.values[max_depth - curr_depth + 1], curr_nums[0] // 2 + max_depth - curr_depth)
    # but if this is the last number, it should not apply
    if curr_depth == max_depth:
        i = min_value_depth.values[max_depth - curr_depth + 1]
    # continue until going over max number possible
    while i < last:
        # set the new list
        next_nums = curr_nums + [i]
        # check if valid as a special sum set
        if not is_special_sum_set(next_nums,
                                  subsets_sums=set(list(curr_subsets_sums) + [i + k for k in curr_subsets_sums]),
                                  is_sorted_big_to_small=True):
            i += 1
            continue
        # call the next depth
        new_max_sum = None if max_sum is None else max_sum - i
        res = rec(next_nums, set(list(curr_subsets_sums) + [k + i for k in curr_subsets_sums]),
                  max_depth, new_max_sum, min_value_depth)
        # if we found a first solution, or a better solution that the current
        if res is not None and (best_found is None or sum(best_found) > sum(res)):
            best_found = res
            # update the last and max_sum to fit to the new best solution
            max_sum = None if max_sum is None else sum(best_found)
            if max_sum is not None:
                last = min(last, max_sum - min_value_depth.sums[max_depth - curr_depth])
        i += 1
    return best_found
