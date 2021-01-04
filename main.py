import time

from solution_file.solution_file_creator import add_problem_solution
from problems.P067 import ans

start_time = int(round(time.time() * 1000))
print(ans())
# add_problem_solution(61, override=True)
print((int(round(time.time() * 1000)) - start_time) / 1000, "seconds")
