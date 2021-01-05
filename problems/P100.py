# using diophantine equations
def ans():
    """
    x is number of blue disks, t is number of total disks. so:
    (x^2-x)/(t^2-t)=1/2, so:
    2x^2-2x+t-t^2=0
    solution:
    x0=1,t0=1
    and:
    x[n+1]=3xn+2tn-2
    t[n+1]=4xn+3tn-3
    *****
    or:
    x[n+1]=3xn-2tn
    t[n+1]=-4xn+3tn+1
    but second side's t is always negative, so ignore it
    *****
    """
    low_bound = 10 ** 12
    first_side: (int, int) = (1, 1)
    while first_side[1] < low_bound:
        xn = first_side[0]
        tn = first_side[1]
        first_side = (3 * xn + 2 * tn - 2, 4 * xn + 3 * tn - 3)
    return first_side[0]
