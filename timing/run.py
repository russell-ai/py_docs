#run.py
import timing

code = "[a**3 for a in range(100)]"
print (code)
result=timing.timeit(code,100)
print(result)


