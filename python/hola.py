def fib(n):
    if n == 1:
        return 1
    elif n==2:
        return 2
    else:
        return fib(n-2)+fib(n-1)
    print(fib(27))