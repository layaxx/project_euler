# sum of all the amicable numbers under 10000.
import math
import datetime

def solveWithCache(limit = 10000):
    cache = []
    sum = 0
    for a in range(1, limit + 1):
        if a not in cache:
            b = sumOfDivisors(a)
            if sumOfDivisors(b) == a and a != b:
                sum += a
                sum += b
                cache.append(b)
    #print(sum)

def solveWithoutCache(limit = 10000):
    sum = 0
    for a in range(1, limit + 1):
        b = sumOfDivisors(a)
        if sumOfDivisors(b) == a and a != b:
            sum += a
    #print(sum)


def sumOfDivisors(number):
    sum = 0
    i = 1
    while i <= math.sqrt(number): 
          
        if (number % i == 0) : 
            sum += i
            # If divisors are equal, print only one 
            if not (number / i == i or number/i == number) : 
                sum += number/i
        i = i + 1

    return int(sum)


def testAlgorithms():
    start = datetime.datetime.now()
    for x in range(1, 8):
        solveWithCache(int(math.pow(10, x)))
    durationWithCache = datetime.datetime.now() - start

    start = datetime.datetime.now()
    for x in range(1, 8):
        solveWithoutCache(int(math.pow(10, x)))
    durationWithoutCache = datetime.datetime.now() - start

    print("Duration without Cache: " + str(durationWithoutCache))
    print("Duration with Cache: " + str(durationWithCache))
    print("Cache saves " + str(1 - (durationWithCache/durationWithoutCache)))


testAlgorithms()

