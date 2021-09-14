from math import log


def ans():
    """
    analyzing the first values for p(123,n),
    we see that the powers jump only in one of these diffs: {196, 289, 485}.

    if n is a value for p(123,x)=n then there exists a k s.t.:
    2^n = 1.23...*10^k
    take log10 on both sides:
    n*log10(2) = k+log10(1.23...)
    so:
    k = n*log10(2)-log10(1.23...)
    that means that n is a solution if k is an integer

    in my opinion, this solution is nasty and relies on no rounding errors, rather that pure algorithms.
    """
    count = 1
    n = 90
    log123 = log(1.23, 10)
    diff = log(1.24, 10) - log123
    log2 = log(2, 10)
    while count < 678910:
        for jump in [196, 289, 485]:
            temp_n = n + jump
            k = temp_n * log2 - log123
            if k - int(k) < diff:  # and also k-int(k)>0 for sure
                count += 1
                n += jump
                break
    return n
