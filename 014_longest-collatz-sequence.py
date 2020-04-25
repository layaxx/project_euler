# n is even => n = n/2
# n is odd => n = 3n + 1

def solve():
    bestStartingNumber = 1
    maxLength = 0

    for i in range(1, 1000000):
        currentLength = getLenghtOfCollatzSequenceFor(i)
        if currentLength > maxLength:
            bestStartingNumber = i
            maxLength = currentLength

    print("longest chain for starting numbers under one million produced by " + str(bestStartingNumber))


def getLenghtOfCollatzSequenceFor(number):
    length = 1
    while number != 1:
        if number % 2 == 0:
            number *= 0.5
        else:
            number = number * 3 + 1
        length += 1
    return length


solve()
