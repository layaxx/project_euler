""" The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator. """

import math
from fractions import Fraction

def solve():
    fractions = []
    for denominator in range(10, 100):
        for  numerator in range(10, denominator):
            fraction = numerator / denominator
            if isNonTrivialCuriousFractions(numerator, denominator):
                print((numerator, denominator))
                fractions.append((numerator, denominator))

    numerator = 1
    denominator = 1
    for fraction in fractions:
        numerator *= fraction[0]
        denominator *= fraction[1]

    finalFraction = Fraction(numerator, denominator)

    print(finalFraction)

def isNonTrivialCuriousFractions(numerator, denominator):
    fraction = numerator / denominator
    digit0 = int(str(numerator)[0])
    digit1 = int(str(numerator)[1])
    digit2 = int(str(denominator)[0])
    digit3 = int(str(denominator)[1])


    if "0" in str(numerator) and "0" in str(denominator):
        return False

    if str(numerator)[0] == str(denominator)[0]:
        if digit3 != 0:
            if digit1 / digit3 == fraction:
                return True

    if str(numerator)[0] == str(denominator)[1]:
        if digit2 != 0:
            if digit1 / digit2 == fraction:
                return True

    if str(numerator)[1] == str(denominator)[0]:
        if digit3 != 0:
            if digit0 / digit3 == fraction:
                return True

    if str(numerator)[1] == str(denominator)[1]:
        if digit2 != 0:
            if digit0 / digit2 == fraction:
                return True

    return False

solve()