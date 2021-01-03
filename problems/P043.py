from libs.numbers_properties import num_size


def ans():
    # create all numbers this way
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    primes_list = [2, 3, 5, 7, 11, 13, 17]
    all_numbers = []

    def create_nums(num):
        if num_size(num) == 10:
            all_numbers.append(num)
        if num == 0:
            for i in range(1, 10):
                create_nums(i)
        else:
            for i in digits:
                if str(i) not in str(num):
                    if num_size(num * 10 + i) > 3:
                        if ((num * 10 + i) % 1000) % primes_list[num_size(num * 10) - 4] == 0:
                            create_nums(num * 10 + i)
                    else:
                        create_nums(num * 10 + i)

    create_nums(0)
    return sum(all_numbers)
