from solution.libs.files import get_file_lines
from itertools import combinations, permutations
from tqdm import tqdm
from solution.libs.numbers_properties import is_square
from solution.libs.types_converting import list_to_string, string_to_list


def ans():
    words_list = make_words_list()
    # get only words that have matching anagram
    anagrams = get_repeated_anagrams(words_list)
    anagrams_pairs = []
    for i in anagrams:
        anagrams_pairs += combinations(i, 2)
    # now handle each order
    max_of_each_pair = []
    for i in tqdm(anagrams_pairs):
        vals = values_from_pair(i)
        if len(vals) != 0:
            max_of_each_pair.append(max(vals))
    return max(max_of_each_pair)


def make_words_list():
    words_list = get_file_lines("P098")[0].split(",")
    for i in range(len(words_list)):
        words_list[i] = (list_to_string(sorted(string_to_list(words_list[i].strip("\"")))), words_list[i].strip("\""))
    return words_list


def get_repeated_anagrams(words_list):
    anagrams = dict()
    for i in words_list:
        if i[0] in anagrams.keys():
            anagrams[i[0]].append(i[1])
        else:
            anagrams[i[0]] = [i[1]]
    return [anagrams[k] for k in anagrams.keys() if len(anagrams[k]) > 1]


def values_from_pair(p):
    results = []
    w1 = p[0]
    w2 = p[1]
    chars = list(set(string_to_list(w1)))  # chars without repetition
    chars_without_forbidden_zeroes = list(set(chars).difference({w1[0], w2[0]}))
    chars_values = dict()
    for first_letters_perm in permutations([i for i in range(1, 10)], 2):
        chars_values[w1[0]] = first_letters_perm[0]
        chars_values[w2[0]] = first_letters_perm[1]
        for perm in permutations(list(set([i for i in range(10)]).difference(set(first_letters_perm))),
                                 len(chars_without_forbidden_zeroes)):
            for j in range(len(chars_without_forbidden_zeroes)):
                chars_values[chars_without_forbidden_zeroes[j]] = perm[j]
            n1 = 0
            for c in w1:
                n1 *= 10
                n1 += chars_values[c]
            if not is_square(n1):
                continue
            n2 = 0
            for c in w2:
                n2 *= 10
                n2 += chars_values[c]
            if not is_square(n2):
                continue
            results.append(max(n1, n2))
    return results
