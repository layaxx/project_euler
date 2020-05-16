# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

import math

def solve(power):
    limit = 1000000
    sum = 0

    for i in range(2, limit + 1):
        if canBeWrittenAsSumOfPowers(i, power):
            sum += i

    print(sum)

def canBeWrittenAsSumOfPowers(number, power):
    sum = 0
    for digit in str(number):
        sum += math.pow(int(digit), power)
        if sum > number:
            return False

    return sum == number

solve(5)



'''
What should the limit be?

9 => 9^5 = 59049

each digit can add a max of 59049 to the sum.

at what point does another digit add more to the original number than 59049

is limit = 100,000 enough?

99999 => 5 * 59049 = 295245

no, higher limit is needed.



9^5 * digits < Sum i = 0 to digits: 9 * 10^i


'''