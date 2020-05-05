""" Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0. """

import math

def solve():
    maxChain = 0;
    product = 1;

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            chainLength = getChainLength(a, b);
            if chainLength > maxChain:
                maxChain = chainLength
                product = a * b

    print(product)


def getChainLength(a, b):
    count = 0
    while(isPrime(math.pow(count, 2) + a * count + b)):
        count += 1
    return count

def isPrime(number):
    if number < 2:
        return False
    limit = math.sqrt(number)
    for i in range(2, int(limit  + 1)):
        if number % i == 0:
            return False
    return True



solve()