# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
from num2words import num2words

def solve(limit):
    result = 0
    for number in range(1, limit + 1):
        result += getNumberOfLettersIn(number)
        #print(getNumberOfLettersIn(number))

    print(result)


def getNumberOfLettersIn(number):
    return len("".join("".join(num2words(number).split("-")).split(" ")))


solve(1000)



