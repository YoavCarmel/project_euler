def smallest_number_with_digit_sum(n: int) -> int:
    """
    :param n: wanted digits sum
    :return: smallest number with input digits sum
    """
    return int(str(n % 9) + "9" * (n // 9))

