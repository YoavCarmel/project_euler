from math import factorial


def ans():
    chain_length = dict()
    max_i = 10 ** 6
    for i in range(max_i + 1):
        chain = list()
        j = i
        while j not in chain and j not in chain_length.keys():
            chain.append(j)
            j = fact_digits(j)
        if j in chain_length.keys():
            plus_s = 1
            for k in reversed(chain):
                chain_length[k] = chain_length[j] + plus_s
                plus_s += 1
        else:  # j in chain
            loop_start = chain.index(j)
            for k in range(loop_start):
                chain_length[chain[k]] = len(chain) - k
            for k in range(loop_start, len(chain)):
                chain_length[chain[k]] = len(chain) - loop_start
    return len([i for i in chain_length.keys() if chain_length[i] == 60])


def fact_digits(n):
    s = 0
    while n > 0:
        s += factorial(n % 10)
        n //= 10
    return s
