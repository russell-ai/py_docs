
def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-2)+fib(n-1)

number=int(input("enter a number:"))
for i in range(1,number+1):
    # print(f"{i}.fibonnici number is :{fib(i)}")
    # print("{a}.fibonnici number is :{b}".format(a=i, b=fib(i)))
    # print("{0}.fibonnici number is :{1}".format(i, fib(i)))
    print("%d.fibonnici number is :%d"%(i, fib(i)))