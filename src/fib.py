# 0 1 2 3 4 5 6 7  8  9  10
# 0 1 1 2 3 5 8 13 21 34 55 ... Fibonacci sequence -- each number is the sum of the previous two numbers

# fib(0): 0
# fib(1): 1
# fib(n): fin(n-1) + fib(n-2)

cache = {}

def fib(n):
    if n == 0: return 0
    if n == 1: return 1

    if n not in cache:
        cache[n] = fib(n-1) + fib(n-2)

    return cache[n]     # O(n) over n

for i in range(10):
    print(f"{i:3} {fib(i)}")