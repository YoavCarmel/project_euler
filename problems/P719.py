from tqdm import trange


def ans():
    digits = 12
    s = 0
    # for each sqrt, check if we can create its square from spreading its digits
    for sqrt_num in trange(2, 10 ** (digits // 2) + 1):
        if rec(sqrt_num, sqrt_num ** 2):
            s += sqrt_num ** 2
    return s


def rec(sqrt_num: int, full_num: int, power_10_mod: int = 10) -> bool:
    """
    We want to take full_num's digits apart such that the parts' sum is sqrt_num.
    In each time, we have a choice: whether to take the current digits of full_num (full_num%power_10_mod),
    and remove them from sqrt_num, and move forward, OR get one more digit of full_num.
    """
    if sqrt_num > full_num:
        return False
    if full_num % power_10_mod > sqrt_num:
        return False
    if full_num == sqrt_num:
        return True
    return rec(sqrt_num - full_num % power_10_mod, full_num // power_10_mod) or \
           rec(sqrt_num, full_num, power_10_mod * 10)
