""" A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 
28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. """

import math

def solve():
    abundantNumbers = []
    limit = 28123
    for integer in range(12, limit + 1 - 12):
        if sumOfDivisors(integer) > integer:
            abundantNumbers.append(integer)
    print("completed list of abundant Numbers: " + str(len(abundantNumbers)))
    sum = 0
    for integer in range(0, limit + 1):
        if not checkIfSum(integer, abundantNumbers):
            sum += integer

    print(sum)

def checkIfSum(integer, abundantNumbers):
    abundantNummer1 = abundantNumbers[0]
    abundantNummer2 = abundantNumbers[0]
    while abundantNummer1 <= integer / 2:
        while abundantNummer2 + abundantNummer1 <= integer:
            if abundantNummer1 + abundantNummer2 == integer:
                return True
            abundantNummer2 = abundantNumbers[abundantNumbers.index(abundantNummer2) + 1]
        abundantNummer1 = abundantNumbers[abundantNumbers.index(abundantNummer1) + 1]
    return False;


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

solve()