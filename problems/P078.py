from typing import Dict, List

from sympy import divisors


def ans():
    """
    thanks to mathologer's video: https://youtu.be/iJ8pnCO0nTY
    our algorithm will keep track of all found numbers, and calculate the next one based on the prevs.
    the pattern is like that: have another list that contains indices of the list (counting backward from current)
    together with plus/minus for each one, that is created during the run.
    to get the next numebr of partitions each time, we apply the calculation based on the indices in the second list.
    the second list is built like that: start with [(1,+),(2,+)].
    when appending the i'th term:
        value:
            if i is even, append l[i-1]+(i+1)
            if i is odd, append l[i-1]+(i+1)//2
        sign (plus/minus):
            if i%4 is 0 or 1, append +
            if i%4 is 2 or 3, append -
    """
    partitions: List[int] = [1]
    indices: List[(int, int)] = [(1, 1), (2, 1)]
    i = 1
    while len(partitions) < 5 or partitions[-1] % 10 ** 6 != 0:
        # get new partition
        s = 0
        for value in indices[:-1]:
            s += partitions[i - value[0]] * value[1]
        partitions.append(s)
        # check if need to add a new value to indices
        if indices[-1][0] == i:
            indices_len = len(indices)
            if indices_len % 4 == 0:
                indices.append((indices[-1][0] + indices_len + 1, 1))
            if indices_len % 4 == 1:
                indices.append((indices[-1][0] + (indices_len + 1) // 2, 1))
            if indices_len % 4 == 2:
                indices.append((indices[-1][0] + indices_len + 1, -1))
            if indices_len % 4 == 3:
                indices.append((indices[-1][0] + (indices_len + 1) // 2, -1))
        i += 1
    return i - 2

# def ans():
#     print("takes about 4 minutes")
#     # p(n)=1/n* (sum from k=0 to n-1 of p(k)*dv_sum(n-k))
#     dv_sum: Dict[int] = dict()
#     p: Dict[int] = dict()
#     p[0] = 1
#     n = 1
#     thresh = 10 ** 6
#     while True:
#         print(n)
#         dv_sum[n] = sum(divisors(n))
#         s = 0
#         for k in range(0, n):
#             s += dv_sum[n - k] * p[k]
#         s //= n
#         if s % thresh == 0:
#             return n
#         p[n] = s
#         print(n,s)
#         n += 1

# too slow
# def ans():
#     thresh = 10 ** 6
#     # a[i][j] is number of partitions with sum i and biggest number is j
#     a: Dict[int, Dict[int, int]] = defaultdict(dict)
#     a[0][0] = 1
#     i = 1
#     while True:
#         print(i)
#         a[i][0] = 0
#         for j in range(1, i + 1):
#             # either put j and handle the rest, or dont put j and lower it by 1
#             a[i][j] = a[i - j][min(i - j, j)] + a[i][j - 1]
#         if i>1 and (a[i][i]-1)%thresh==0:
#             return i
#         i += 1
