def is_any_case_letter(c: chr) -> bool:
    """
    :param c: a character
    :return: True if the input char is an english letter, False otherwise
    """
    return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z')


def is_number_char(c: chr) -> bool:
    """
    :param c: a character
    :return: True if the input char is an english letter, False otherwise
    """
    return ord('0') <= ord(c) <= ord('9')
