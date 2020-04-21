# sum of all the primes below two million

import math 

def solve(limit = 2000000):
    sum = 0
    prime = 2
    while prime < limit:
        sum += prime
        prime = getNextPrimeNumber(prime)
    print(sum)


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
