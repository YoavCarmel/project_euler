from typing import List


def is_palindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]


def all_palindromes_n_digits(n: int) -> List[int]:
    if n % 2 == 1:
        if n == 1:  # special case
            return list(range(1, 10))
        # e.g. for n=7 do all "abcd"+"cba"
        return [int(str(num) + str(num // 10)[::-1]) for num in range(10 ** (n // 2), 10 ** (n // 2 + 1))]
    else:
        # e.g. for n=6 do all "abc"+"cba"
        return [int(str(num) + str(num)[::-1]) for num in range(10 ** (n // 2 - 1), 10 ** (n // 2))]


def all_palindromes_up_to_n_digits(n: int) -> List[int]:
    return [num for d in range(1, n + 1) for num in all_palindromes_n_digits(d)]
