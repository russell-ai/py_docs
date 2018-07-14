
from functools import wraps
from time import perf_counter
def timed(n):
    def decorated(fn):
        count=0
        total_elapsed=0
        def inner(*args, **kwargs):
            """
            This function is closure and arguments belong to fn function
            """
            nonlocal n,count,total_elapsed
            for i in range(n):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed+= (end-start)
                count+=1
            print("{0} function took average {1:6f} milisecond for the {2} times and result:{3}".format(fn.__name__, (total_elapsed), count, result))
            return result
        return inner
    return decorated
@timed(3)
def fib(x):
    a=1
    b=1
    for i in range(3,x+1):
        a,b=b,a+b
    return b
if __name__== "__main__":
    fib(25)