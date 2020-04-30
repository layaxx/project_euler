# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

def solve():
    limit = 1000
    fib1 = 1
    fib2 = 1
    count = 2
    while(len(str(fib2)) < 1000):
        tmp = fib1
        fib1 = fib2
        fib2 = fib1 + tmp
        count += 1
    print(count)





solve()