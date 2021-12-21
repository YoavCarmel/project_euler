import pandas as pd
import pytest

from main_functions.problem_runner import run
from main_functions.solution_file_handler import get_all_problems, SOLUTION_FILE_PATH, PROBLEM_NUM, SOLUTION

solutions = pd.read_csv(SOLUTION_FILE_PATH)


@pytest.mark.parametrize("problem_num", get_all_problems())
def test_run_all(problem_num):
    result = run(problem_num)
    assert float(result) == solutions[solutions[PROBLEM_NUM] == problem_num][SOLUTION].values[0]
