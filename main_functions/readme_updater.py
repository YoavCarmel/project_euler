from typing import List, Union

import pandas as pd


def update_readme(problems_solved: Union[pd.Series, List[int]]):
    with open("README.md", "r") as f:
        lines = f.readlines()
    header_line = f"## Solved problems (total {len(problems_solved)}):\n"
    problems_line = str(sorted(problems_solved)) + "\n"
    header_index = _get_header_index(lines, "## Solved problems")
    if header_index is not None:
        lines[header_index] = header_line
        if len(lines) == header_index + 1:
            # this is the last line, add a new one
            lines.append(problems_line)
        else:
            problems_index = None
            for i, line in enumerate(lines[header_index + 1:]):
                if line.strip() != "":
                    problems_index = i + header_index + 1
            lines[problems_index] = problems_line
    else:  # if no record in file:
        lines.append(header_line)
        lines.append(problems_line)
    with open("README.md", "w") as f:
        f.writelines(lines)


def _get_header_index(lines: List[str], prefix: str):
    for i, line in enumerate(lines):
        if line.startswith(prefix):
            return i
    return None
