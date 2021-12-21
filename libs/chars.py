def is_any_case_letter(c: chr) -> bool:
    """
    :param c: a character
    :return: True if the input char is an english letter, False otherwise
    """
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'


def is_number_char(c: chr) -> bool:
    """
    :param c: a character
    :return: True if the input char is an english letter, False otherwise
    """
    return '0' <= c <= '9'
