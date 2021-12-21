import pytest

from main_functions.problem_runner import run
from main_functions.solution_file_handler import get_all_problems


@pytest.mark.parametrize("problem_num", get_all_problems())
def test_run_all(problem_num):
    run(problem_num)
