import time

from main_functions.runs_helper import get_import_line, get_run_line


def run(problem_number):
    exec(get_import_line(problem_number))
    start_time = time.time()
    print(eval(get_run_line(problem_number)))
    print(round(time.time() - start_time, 3), "seconds")
