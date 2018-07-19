#timing.py
"""
    This module takes the code and run n times the code
    and gives the elapsed time.
    """
from time import perf_counter
from collections import namedtuple
import  argparse


Timing=namedtuple("Timing", "repeats elapsed evarege")

def timeit(code, repeats=10):
    code = compile(code,filename="<string>",mode="exec")
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end-start
    evarege = elapsed/repeats
    return Timing(repeats, elapsed, evarege)

if __name__ == "__main__":
    # Get the code from arguments
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("code", type=str, help="The python code snippet")
    parser.add_argument("-r", "--repeats", type=int, default=10, help="Number of times to run the code")
    args = parser.parse_args()
    print(f"timing: {args.code}...")
    print(timeit(code=str(args.code),repeats=args.repeats))
