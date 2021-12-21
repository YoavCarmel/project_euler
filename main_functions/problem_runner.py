import sys

import pandas as pd
import time

from tqdm import tqdm

from main_functions.runs_helper import get_import_line, get_run_line
from main_functions.solution_file_handler import PROBLEM_NUM


def run(problem_number):
    exec(get_import_line(problem_number))
    start_time = time.time()
    print(eval(get_run_line(problem_number)))
    print(round(time.time() - start_time, 3), "seconds")


def run_all():
    all_problems = list(pd.read_csv("solution_file.csv")[PROBLEM_NUM])
    for problem_num in tqdm(all_problems):
        print(f"{problem_num=}")
        try:
            run(problem_num)
        except Exception as e:
            print("ERROR", e)
        print()
