import time


def Fib(n):
    prev = 0
    current = 1
    for i in range(n):
        tmp = current
        current = current + prev
        prev = tmp
    return current


def recursiveFib(n):
    if n <= 1:
        return 1
    else:
        return recursiveFib(n - 1) + recursiveFib(n - 2)


def FibAnalysis(n):
    current = time.time_ns()
    Fib(n)
    elapsed = time.time_ns() - current
    print("Time taken to determine the {}th Fibonacci number non-recursively: {} nanoseconds.".format(n, elapsed))

    current = time.time_ns()
    recursiveFib(n)
    elapsed = time.time_ns() - current
    print("Time taken to determine the {}th Fibonacci number recursively: {} nanoseconds.".format(n, elapsed))


FibAnalysis(40)

# The non-recursive function is much more efficient because in the recursive function, you must recall up to 2 more
# functions for every recursive call, and this is inefficient because it calls the same numbers multiple times. In
# the non-recursive function, it calls all fibonacci numbers up to n linearly, making it take the least number of steps
# to determine the nth fibonacci number. 
