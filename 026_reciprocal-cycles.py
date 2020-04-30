# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


# Die Anzahl der periodischen Kommastellen beim Nenner m wird gegeben durch die kleinste Zahl n, bei der die Division von 10n durch m den Rest 1 ergibt.
#   Assumptions:
#   1:  Die Anzahl der periodischen Kommastellen beim Nenner m wird gegeben durch die kleinste Zahl n, bei der die Division von 10^n durch m den Rest 1 ergibt.
#   2:   Nur Brüche, deren Nenner (im vollständig gekürzten Zustand) keine anderen Primfaktoren als 2en und/oder 5en besitzen, ergeben einen unperiodischen Dezimalbruch, der eine endliche Zahl an Kommastellen besitzt.
# source: https://www.arndt-bruenner.de/mathe/scripts/periodenlaenge.htm



import math

def solve():
    longest = 0
    for i in range(2,1000):
        if recCycle(i) > longest:
            longest = i
    print(longest)


def recCycle(number):
    if otherPrimeFactors(number):
        return 0
    n = 1
    rest = 10 % number
    reste = []
    reste.append(rest)
    while rest != 1:
        rest = rest*10
        rest = rest % number
        if reste.count(rest) != 0:
            return n
        reste.append(rest)
        n += 1
    return n

# adapted from: https://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
def otherPrimeFactors(number):
    while number % 2 == 0: 
        number = number / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(number))+1,2): 
        # while i divides n , print i and divide n 
        while number % i== 0: 
            if i != 5:
                return False
            number = number / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if number > 2: 
        if number != 5:
            return False
    return True


solve()

# print(recCycle(6))
