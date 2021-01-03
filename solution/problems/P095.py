from sympy import divisors


def ans():
    print("takes about 15 seconds, i didnt want to improve it")
    max_chain = []
    million = 10 ** 6
    checked = set()
    for i in range(1, million + 1):
        if i in checked:
            continue
        chain_s = set()
        chain_l = list()
        s = i
        while s not in chain_s and s <= million and s not in checked:
            checked.add(s)
            chain_s.add(s)
            chain_l.append(s)
            s = D(s)
        if s > million:
            continue
        if s in checked and s not in chain_s:
            continue
        length = len(chain_l) - chain_l.index(s)
        if length > len(max_chain):
            max_chain = chain_l[chain_l.index(s):]
    return min(max_chain)


def D(x):
    return sum(divisors(x)) - x
