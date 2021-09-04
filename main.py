import time

from problems.P165 import ans
from solution_file.solution_file_creator import add_problem_solution

start_time = int(round(time.time() * 1000))
print(ans())
# add_problem_solution(165, override=True)
print((int(round(time.time() * 1000)) - start_time) / 1000, "seconds")
