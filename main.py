import time

from solution_file.solution_file_creator import add_problem_solution
from libs.calculations import fibonnaci_number_by_index
from problems.P120 import ans

start_time = int(round(time.time() * 1000))
print(ans())
# add_problem_solution(118, override=True)
print((int(round(time.time() * 1000)) - start_time) / 1000, "seconds")
