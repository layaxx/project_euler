from datetime import datetime
import random

def solve():

    count = 1
    triangular = 0
    best = 1
    divisors = 0

    while(divisors <= 500):
        triangular += count
        count += 1
        divisors = getNumberOfDivisors(triangular)
        best = max(best, divisors)
        if count % 100 == 0:
            print("Still doing shit: " + str(count) +
                  " highest so far: " + str(best) + " divisors")
    print(triangular)

# original Solution (seems to work correctly, but takes like 3 hours (honestly, maybe more))
def getNumberOfDivisorsSlow(number):
    divisors = 1
    for div in range(1, int(number /2 )+ 1):
        if number % div == 0:
            divisors += 1
    return divisors

# copied from StackOverflow
def getNumberOfDivisors(n):
    count = 2  
    i = 2
    while i ** 2 < n:
        if n % i == 0:
            count += 2
        i += 1
    if i ** 2 == n:
        count += 1
    return count
    
solve()








# some analysis of the algorithms
def testFunctions():
    # get random numbers
    totalBetter = datetime.now() - datetime.now()
    totalWorse = datetime.now() - datetime.now()

    for times in range(0, 5):
        randomNumbers = []
        for x in range(0, 10):
            randomNumbers.append(random.getrandbits(max(3,random.getrandbits(5))))
            print("generated new random Number: " + str(randomNumbers[x]))
        startTime = datetime.now()
        for x in randomNumbers:
            getNumberOfDivisorsSlow(x)
        totalWorse += datetime.now() - startTime
        startTime = datetime.now()
        for x in randomNumbers:
            getNumberOfDivisors(x)
        totalBetter += datetime.now() - startTime
    
    print("Results:")
    print("Better Algorithm: " + str(totalBetter / 50))
    print("My Algorithm: " + str(totalWorse / 50))
    print("My Algorithm took " + str((totalWorse / 50)/(totalBetter / 50))+ " times as long")

# testFunctions()