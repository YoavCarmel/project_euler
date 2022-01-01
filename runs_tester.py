import pytest

from main_functions.problem_runner import run
from main_functions.solution_file_handler import get_all_problems, PROBLEM_NUM, SOLUTION, read_solutions_file

solutions = read_solutions_file()


@pytest.mark.parametrize("problem_num", get_all_problems())
def test_run_all(problem_num):
    result = run(problem_num)
    assert str(result) == solutions[solutions[PROBLEM_NUM] == problem_num][SOLUTION].values[0]
