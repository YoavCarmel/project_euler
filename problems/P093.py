from collections import Counter
from itertools import permutations, combinations_with_replacement, combinations, product
from typing import List, Tuple, Optional

from tqdm import trange, tqdm

from libs.types_converting import list_to_num

BracketsPositions = List[Tuple[int, int]]
BracketsTemplate = Tuple[List[str], List[int], List[int]]
BracketsOpersTemplate = Tuple[List[str], List[int]]
Quad = Tuple[int, int, int, int]


def ans():
    brackets = [
        [], [(1, 2)], [(2, 3)], [(3, 4)], [(1, 3)], [(2, 4)], [(1, 2), (3, 4)], [(1, 2), (1, 3)],
        [(2, 3), (1, 3)], [(2, 3), (2, 4)], [(3, 4), (2, 4)]
    ]
    brackets_templates = [generate_brackets_template(brack) for brack in brackets]
    operators = ["+", "-", "*", "/"]
    brackets_opers_template = [template for brackets_template in brackets_templates for template in
                               generate_brackets_opers_template(operators, brackets_template)]
    m: Tuple[int, Optional[Quad]] = (-1, None)
    # although 0 is a digit, there is no point including it in this
    for a, b, c, d in tqdm(combinations(list(range(1, 10)), 4)):
        quad = (a, b, c, d)
        m = max(m, (calc(quad, brackets_opers_template), quad))
    return list_to_num(sorted(m[1]))


def calc(nums: Quad, brackets_opers_templates: List[BracketsOpersTemplate]):
    results = set()
    nums = [str(i) for i in nums]
    for (template, nums_indices), nums_perm in product(brackets_opers_templates, permutations(nums)):
        for ni, n in zip(nums_indices, nums_perm):
            template[ni] = n
        try:
            s = "".join(template)
            results.add(eval(s))
        except ZeroDivisionError:
            continue
    i = 1
    while i in results:
        i += 1
    return i


def generate_brackets_template(brack: BracketsPositions) -> BracketsTemplate:
    """
    :param brack: a list of pairs of brackets
    :return: the template for these brackets, and a list of nums indices and a list of operators indices in the template
    """
    br_start = Counter(br[0] for br in brack)
    br_end = Counter(br[1] for br in brack)
    res = []
    nums_indices = []
    opers_indices = []
    res.append("(" * br_start.get(1, 0))
    # first num
    nums_indices.append(len(res))
    res.append("n")
    # first operator
    opers_indices.append(len(res))
    res.append("o")
    res.append("(" * br_start.get(2, 0))
    # second num
    nums_indices.append(len(res))
    res.append("n")
    res.append(")" * br_end.get(2, 0))
    # second operator
    opers_indices.append(len(res))
    res.append("o")
    res.append("(" * br_start.get(3, 0))
    # third num
    nums_indices.append(len(res))
    res.append("n")
    res.append(")" * br_end.get(3, 0))
    # third operator
    opers_indices.append(len(res))
    res.append("o")
    # fourth num
    nums_indices.append(len(res))
    res.append("n")
    res.append(")" * br_end.get(4, 0))
    return res, nums_indices, opers_indices


def generate_brackets_opers_template(operators: List[str], brackets_templates: BracketsTemplate) \
        -> List[BracketsOpersTemplate]:
    res: List[BracketsOpersTemplate] = list()
    template, nums_indices, opers_indices = brackets_templates
    for opers in combinations_with_replacement(operators, 3):
        for oi, o in zip(opers_indices, opers):
            template[oi] = o
        res.append((template.copy(), nums_indices))
    return res
