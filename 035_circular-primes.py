""" The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million? """

import math

limit = 1000000

primeList = [0] * limit # 0 for not checked yet, 1 for Prime, 2 for not Prime

def solve():
    count = 0

    for i in range(1, limit):
        if primeList[i] == 0:
            primeList[i] = isPrime(i)
        if primeList[i] == 1:
            if check(i):
                count += 1
    
    print(count)

def isPrime(n):
    # return 1 if n is Prime, 2 if not
    for i in range(2, int(math.sqrt(n)) + 1):
        if(n%i == 0):
            return 2
    if n < 2:
        return 2
    return 1

def check(n):
    # check if all rotations of n are prime
    number = n
    for i in range(len(str(n))):
        number = (int(str(number)[-1] + str(number)[:-1]))
        if primeList[number] == 0:
            primeList[number] = isPrime(number)
        if  primeList[number] == 2:
            return False
            
    return True
    

solve()