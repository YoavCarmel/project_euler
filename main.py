import time

from problems.P120 import ans

start_time = int(round(time.time() * 1000))
print(ans())
# add_problem_solution(118, override=True)
print((int(round(time.time() * 1000)) - start_time) / 1000, "seconds")
