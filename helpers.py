import inspect
import sys


def iterate_lines_in_file():
    caller_path = inspect.getframeinfo(sys._getframe(1)).filename
    caller_filename = caller_path.split("\\")[-1]
    data_filename = caller_filename.split(".")[0] + ".in"

    print(f"Using {data_filename}")

    with open(data_filename, "rt") as f:
        for line in f.read().strip().split("\n"):
            yield line
