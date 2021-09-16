from collections import defaultdict

from tqdm import trange


def ans():
    digits = 12
    s_nums = 0
    values_dict_power = 6
    values_dict_max = 10 ** values_dict_power
    values_dict = get_values_dict(values_dict_power)
    for sqr in trange(4, 10 ** (digits // 2) + 1):
        if is_s_num(sqr, values_dict, values_dict_max):
            s_nums += sqr ** 2
    return s_nums


def is_s_num(num, values_dict, values_dict_max):
    squared = num ** 2

    # we want to find a split for squared s.t. its sum is num
    def rec_split(num_left, curr_power10, curr_sum):
        # stop condition
        if curr_power10 > num_left:
            return curr_sum + num_left == num
        if curr_sum > num or num_left + curr_sum < num:
            return False
        if num_left < values_dict_max:
            return (num - curr_sum) in values_dict[num_left]
        # choose to split here or not
        return \
            rec_split(num_left // curr_power10, 10, curr_sum + num_left % curr_power10) or \
            rec_no_split(num_left, curr_power10 * 10, curr_sum)

    def rec_no_split(num_left, curr_power10, curr_sum):
        # stop condition
        if curr_power10 > num_left:
            return curr_sum + num_left == num
        if num_left % curr_power10 + curr_sum > num:
            return False
        # choose to split here or not
        return \
            rec_split(num_left // curr_power10, 10, curr_sum + num_left % curr_power10) or \
            rec_no_split(num_left, curr_power10 * 10, curr_sum)

    return rec_split(squared, 10, 0)


def get_values_dict(digits):
    values_dict = defaultdict(set)

    for num in trange(10 ** digits + 1):
        values_dict[num].add(num)
        p = 10
        while p < num:
            num_dp = num // p
            values_dict[num].update(num_dp + val for val in values_dict[num % p])
            p *= 10
    return values_dict


"""
numpy solutions that are for some reason slower than regular python


def get_values_dict(digits):
    values_dict: Dict[int, np.array] = dict()

    for num in np.arange(10 ** digits + 1, dtype=np.int32):
        to_concat_all = [np.array([num])]
        p = np.int32(10)
        while p < num:
            num_dp = num // p
            to_concat_all.append(values_dict[num % p] + num_dp)
            p *= 10
        values_dict[num] = np.concatenate(to_concat_all)
    return {k: set(v) for k, v in values_dict.items()}


def get_values_dict(digits):
    values_dict_np: Dict[int, np.array] = dict()
    values_dict_set: Dict[int, Set] = dict()

    for num in np.arange(10 ** digits + 1, dtype=np.int32):
        curr_set = {num}
        p = np.int32(10)
        while p < num:
            num_dp = num // p
            curr_set.update(values_dict_np[num % p] + num_dp)
            p *= 10
        values_dict_set[num] = curr_set
        values_dict_np[num] = np.array(list(curr_set), dtype=np.int32)
    return values_dict_set
    
    
def get_values_dict(digits):
    values_dict_np: Dict[int, np.array] = dict()
    values_dict_set: Dict[int, Set] = dict()

    for num in np.arange(10 ** (digits - 1), dtype=np.int32):
        curr_set = {num}
        p = np.int32(10)
        while p < num:
            num_dp = num // p
            curr_set.update(values_dict_np[num % p] + num_dp)
            p *= 10
        values_dict_set[num] = curr_set
        values_dict_np[num] = np.array(list(curr_set), dtype=np.int32)
    for num in np.arange(10 ** (digits - 1), 10 ** digits + 1, dtype=np.int32):
        curr_set = {num}
        p = np.int32(10)
        while p < num:
            num_dp = num // p
            curr_set.update(values_dict_np[num % p] + num_dp)
            p *= 10
        values_dict_set[num] = curr_set
    return values_dict_set
"""
