def roman_to_int(r: str) -> int:
    values = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    s = 0
    for curr_c, next_c in zip(r, r[1:]):
        if values[curr_c] < values[next_c]:
            # like IX
            s -= values[curr_c]
        else:
            s += values[curr_c]
    s += values[r[-1]]  # handle the last one
    return s


def int_to_roman(n: int) -> str:
    s = ""
    mapping = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX',
               5: 'V', 4: 'IV', 1: 'I'}
    sorted_values = sorted(mapping.keys(), reverse=True)
    start_index = 0
    while n > 0:
        for i, val in enumerate(sorted_values[start_index:]):
            if n >= val:
                s += mapping[val]
                n -= val
                start_index += i
                break
    return s
