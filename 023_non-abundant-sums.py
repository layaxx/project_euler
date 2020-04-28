""" A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 
28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. """

# Kinda slow but at least its working

import math

def solve():
    abundantNumbers = []
    limit = 28123
    sum = 0

    isSum = [False] * (limit + 1);

    for integer in range(1, limit + 1):
        if sumOfDivisorsBruteforce(integer) > integer:
            abundantNumbers.append(integer)
    
    for index1 in range(len(abundantNumbers)):
        for index2 in range(len(abundantNumbers)):
            if abundantNumbers[index1] + abundantNumbers[index2] > limit:
                break;
            else:
                isSum[abundantNumbers[index1] + abundantNumbers[index2]] = True

    for number in range(limit + 1):
        if not isSum[number]:
            sum += number

    print(sum)

def sumOfDivisorsBruteforce(number):
    sum = 0
    for i in range(1, number):
        if number % i == 0:
            sum += i        
    return sum

solve()