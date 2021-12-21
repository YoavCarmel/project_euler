from libs.calculations.numbers_properties import is_square


def ans():
    """
    using calculus, the min distance for a,b,c if sqrt(a^2+(b-c)^2)
    but we should also choose which of them is the a
    because a>=b>=c, it is better to put a outside so the squares are more balanced
    """
    count = 0
    big_m = 0
    while count < 10 ** 6:
        big_m += 1
        a = big_m
        for bc in range(2, 2 * a + 1):
            x = bc ** 2 + a ** 2
            if is_square(x):
                count += bc // 2 - max(bc - a - 1, 0)  # add all pairs (b,c) such that b+c=bs, a>=b>=c>=1
    return big_m
