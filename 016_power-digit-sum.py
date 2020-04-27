# sum of the digits of the number 2^1000

def solve(number):
    result = 0
    for digit in str(number):
        result += int(digit)
    print(result)

solve(pow(2, 1000))
