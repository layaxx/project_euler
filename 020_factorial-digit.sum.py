# Find the sum of the digits in the number 100!

def solve(n = 100):
    factorial = 1;
    sum = 0
    for i in range(2, n + 1):
        factorial *= i
    for digit in str(factorial):
        sum += int(digit)
    print("Sum of digits for " + str(n) + "! is " + str(sum))

solve()