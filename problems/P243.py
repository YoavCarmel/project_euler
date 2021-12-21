from libs.calculations.numbers_theory import totient_euler
from sympy import nextprime, primerange


def ans():
    bar_n = 15499
    bar_d = 94744
    # find an upperbound for the max prime
    curr_prime = 2
    prod = curr_prime
    while True:
        if bar_d * totient_euler(prod) < bar_n * (prod - 1):
            break
        curr_prime = nextprime(curr_prime)
        prod *= curr_prime
    # we found an upper bound
    primes = list(primerange(0, curr_prime + 1))
    all_results = set()

    def get_all_results(curr_index: int = 0, curr_product: int = 1):
        """
        use this function to put all results inside all_results
        :param curr_index: current index of prime
        :param curr_product: the current product
        :return: None
        """
        all_results.add(curr_product)
        for i in range(curr_index, len(primes)):
            if curr_product * primes[i] > prod:
                break
            get_all_results(i, curr_product * primes[i])

    get_all_results()
    all_results = {i for i in all_results if bar_d * totient_euler(i) < bar_n * (i - 1)}
    return min(all_results)
