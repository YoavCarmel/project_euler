from typing import List, Set

from tqdm import trange

from libs.numbers_properties import is_palindrome
from math import sqrt


def ans():
    print("takes about 18 seconds")
    n = 10 ** 8
    squares: List[int] = [0]
    res: Set[int] = set()
    # create array of sums of squares
    for i in range(1, int(sqrt(n)) + 1):
        squares.append(i ** 2 + squares[-1])
    # go over of subsequences ant check if palindromes
    for i in trange(1, len(squares)):
        for j in range(i - 1):
            x = squares[i] - squares[j]
            if is_palindrome(x) and x < n:
                res.add(x)
    return sum(res)


"""def ans():
    number_of_digs=8
    l = all_palindromes_up_to_n_digits(number_of_digs)
    squares = [0]
    for i in range(1, int(sqrt(10**number_of_digs)) + 1):
        squares.append(i ** 2 + squares[-1])
    print(squares)
    res = set()
    for i in l:
        if find_pair(squares,i):
            res.add(i)
    return len(res),res

def find_pair(arr, n):
    size = len(arr)
    # Initialize positions of two elements
    i, j = 0, int(pow(n,1/3))
    # Search for a pair
    while i < size and j < size:
        if arr[j] - arr[i] == n and abs(i-j)>=2:
            print(n,i,j)
            return True
        elif arr[j] - arr[i] < n:
            j += 1
        else:
            i += 1
    return False"""
