import sys

import pandas as pd
import time

from tqdm import tqdm

from main_functions.runs_helper import get_import_line, get_run_line, get_run_time
from main_functions.solution_file_handler import PROBLEM_NUM, SOLUTION_FILE_PATH


def run(problem_number):
    exec(get_import_line(problem_number))
    start_time = time.time()
    print(eval(get_run_line(problem_number)))
    end_time = time.time()
    print(get_run_time(start_time, end_time), "seconds")


def run_all():
    all_problems = list(pd.read_csv(SOLUTION_FILE_PATH)[PROBLEM_NUM])
    start_time = time.time()
    for problem_num in tqdm(all_problems):
        print(f"{problem_num=}")
        try:
            run(problem_num)
        except Exception as e:
            print("ERROR", e)
        print()
    print("TOTAL RUNTIME:", get_run_time(start_time), "seconds")
