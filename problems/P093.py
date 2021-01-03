from itertools import permutations, combinations_with_replacement
from typing import List, Tuple

from tqdm import trange


def ans():
    print("after many optimization runs in 12 seconds because of exec function time cost")
    brackets = [[(1, 2)], [(2, 3)], [(3, 4)], [(1, 3)], [(2, 4)], [(1, 2), (3, 4)], [(1, 2), (1, 3)], [(2, 3), (1, 3)],
                [(2, 3), (2, 4)], [(3, 4), (2, 4)], [(1, 4)]]
    operators = ["+", "-", "*", "/"]
    brackets_templates: List[Tuple[List[str], List[int], List[int]]] = list()
    for brack in brackets:
        brackets_templates.append(generate_calculation_template(brack))
    m = (-1, -1)
    for a in trange(10):
        for b in range(a):
            for c in range(b):
                for d in range(c):
                    m = max(m,
                            (calc([a, b, c, d], operators, brackets_templates), int(str(d) + str(c) + str(b) + str(a))))
    return m[1]


def calc(nums, operators, brackets_templates):
    results = set()
    nums = [str(i) for i in nums]
    for template, nums_indices, opers_indices in brackets_templates:
        for opers in combinations_with_replacement(operators, 3):
            for i in range(len(opers_indices)):
                template[opers_indices[i]] = opers[i]
            for p in permutations(nums):
                for i in range(len(nums_indices)):
                    template[nums_indices[i]] = p[i]
                try:
                    s = "".join(template)
                    com = "results.add(" + s + ")"
                    exec(com)
                except ZeroDivisionError:
                    continue
    i = 1
    while i in results:
        i += 1
    return i


def generate_calculation_template(brack: List) -> (List[str], List[int], List[int]):
    res = []
    nums_indices = []
    opers_indices = []
    for br in brack:
        if br[0] == 1:
            res.append("(")
    # first num
    nums_indices.append(len(res))
    res.append("n")
    # first operator
    opers_indices.append(len(res))
    res.append("o")
    for br in brack:
        if br[0] == 2:
            res.append("(")
    # second num
    nums_indices.append(len(res))
    res.append("n")
    for br in brack:
        if br[1] == 2:
            res.append(")")
    # second operator
    opers_indices.append(len(res))
    res.append("o")
    for br in brack:
        if br[0] == 3:
            res.append("(")
    # third num
    nums_indices.append(len(res))
    res.append("n")
    for br in brack:
        if br[1] == 3:
            res.append(")")
    # third operator
    opers_indices.append(len(res))
    res.append("o")
    # fourth num
    nums_indices.append(len(res))
    res.append("n")
    for br in brack:
        if br[1] == 4:
            res.append(")")
    return res, nums_indices, opers_indices
