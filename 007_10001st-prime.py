# 10001st prime number?

import math 

def solve(limit = 10001):
    n = 1
    prime = 2
    while n < limit:
        prime = getNextPrimeNumber(prime)
        n += 1
    print(prime)


def getNextPrimeNumber(current):
    current += 1
    while not isPrime(current):
        current += 1
    return current

def isPrime(num):
    for x in range (2, int(math.sqrt(num)) + 1):
        if num % x == 0:
            return False

    return True 

solve()
