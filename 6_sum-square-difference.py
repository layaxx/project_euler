#(1..100)^2 - (1^2+..+100^2)

def solve(n):
    sum1 = 0
    sum2 = 0
    for x in range(1, n + 1):
        sum1 += x
        sum2 += x*x

    result = (sum1 * sum1) - sum2
    print(result)

solve(100)