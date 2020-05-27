""" 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included. """

# max 7 digits

import math

def solve():
    result = 0

    for i in range(10, 1000000):
        if isCurious(i):
            result += i

    print(result)


def isCurious(input):
    sum = 0

    for digit in str(input):
        sum += math.factorial(int(digit))

    return sum == input


solve()
