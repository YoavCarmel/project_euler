def is_any_case_letter(c: chr) -> bool:
    return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z')


def is_number_char(c: chr) -> int:
    return ord('0') <= ord(c) <= ord('9')
