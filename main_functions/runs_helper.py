from libs.numbers_properties import num_size


def get_file_number(n: int) -> str:
    return "0" * (3 - num_size(n)) + str(n)


def get_import_line(problem_number):
    return f"from problems import P{get_file_number(problem_number)}"


def get_run_line(problem_number):
    return f"P{get_file_number(problem_number)}.ans()"
