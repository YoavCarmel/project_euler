import time

from main_functions.runs_helper import get_import_line, get_run_line, get_run_time


def run(problem_number):
    exec(get_import_line(problem_number))
    start_time = time.time()
    result = eval(get_run_line(problem_number))
    print(result)
    end_time = time.time()
    print(get_run_time(start_time, end_time), "seconds")
    return result  # if needed
