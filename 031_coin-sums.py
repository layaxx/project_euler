""" In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins? """

target = 200
ways = 0

for a in range(target, -1, -200):
    for b in range(a, -1, -100):
        for c in range(b, -1, -50):
            for d in range(c, -1, -20):
                for e in range(d, -1, -10):
                    for f in range(e, -1, -5):
                        for g in range(f, -1, -2):
                           ways += 1

print(ways)


""" def solve():
    options = [1,2,5,10,20,50,100]
    goal = 200

    combinations = [[1],[2],[5],[10],[20],[50],[100]]

    combinationsFinal = [200]

    maxLength = 200 # no combination consist of more than 200 coins [and only one can consist of 200]

    for n in range(maxLength):
        newCombinations = []
        for combination in combinations:
            
            if getTotal(combination) == goal:
                if combinationsFinal.count(combination) == 0:
                    combinationsFinal.append(combination)
            else:
                for option in options:
                    if getTotal(combination) + option <= goal:
                        newCombi = combination.copy()
                        newCombi.append(option)
                        newCombi.sort()
                        if newCombinations.count(newCombi) == 0:
                            newCombinations.append(newCombi)

        combinations = newCombinations.copy()
        print("n = " + str(n))

    for combination in combinations:
        if getTotal(combination) == goal:
            if combinationsFinal.count(combination) == 0:
                combinationsFinal.append(combination)

    print(len(combinationsFinal))
    



def getTotal(combination):
    sum = 0
    for coin in combination:
        sum += coin

    return sum



solve() """