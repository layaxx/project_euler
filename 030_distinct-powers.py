# Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:
# How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?

import math

def solve():

    terms = []

    for a in range(2, 101):
        for b in range(2, 101):
            term = math.pow(a, b)
            if terms.count(term) == 0:
                terms.append(term)

    print(len(terms))



solve()