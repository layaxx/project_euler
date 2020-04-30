# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


import itertools

l = list(itertools.permutations('0123456789', 10))

print(l[999999])

""" I guess you shouldn´t reinvent the wheel... especially if your wheel takes an eternity to run and returns wildly incorrect results.
import math

def solve():
    all = [0,1,2,3,4,5,6,7,8,9]
    
    #total combinations: 10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800
    combinations = []
    #while count <= 1000000:
    for digit in all:
        c2 = all.copy()
        c2.remove(digit)
        for digit2 in c2:
            c3 = all.copy()
            c3.remove(digit2)
            for digit3 in c3:
                c4 = all.copy()
                c4.remove(digit3)
                for digit4 in c4:
                    c5 = all.copy()
                    c5.remove(digit4)
                    for digit5 in c5:
                        c6 = all.copy()
                        c6.remove(digit5)
                        for digit6 in c6:
                            c7 = all.copy()
                            c7.remove(digit6)
                            for digit7 in c7:
                                c8 = all.copy()
                                c8.remove(digit7)
                                for digit8 in c8:
                                    c9 = all.copy()
                                    c9.remove(digit8)
                                    for digit9 in c9:
                                        c10 = all.copy()
                                        c10.remove(digit9)
                                        for digit10 in c10:
                                            combination = str(digit) + str(digit2) + str(digit3) + str(digit4) + str(digit5) + str(digit6) +str(digit7) + str(digit8) + str(digit9) + str(digit10)
                                            flag = False
                                            for n in range(10):
                                                if combination.count(str(n)) != 1:
                                                    flag = True
                                                    break
                                            if flag == False:
                                                combinations.append(combination)
                                                if len(combinations) == 1000000:
                                                    print(combinations[-1])
                                                    return
                                                                                  

def solveNew():
    combination = ""
    combinations = []
    for digit1 in range(10):
        combination = str(digit1)
        for digit2 in range(10):
            if combination.count(str(digit2)) == 0:
                combination += str(digit2)
                for digit3 in range(10):
                    if combination.count(str(digit3)) == 0:
                        combination += str(digit3)
                        for digit4 in range(10):
                            if combination.count(str(digit4)) == 0:
                                continue
                                combination += str(digit4)
                                for digit5 in range(10):
                                    if combination.count(str(digit5)) == 0:
                                        combination += str(digit5)
                                        for digit6 in range(10):
                                            if combination.count(str(digit6)) == 0:
                                                combination += str(digit6)
                                                for digit7 in range(10):
                                                    if combination.count(str(digit7)) == 0:
                                                        combination += str(digit7)
                                                        for digit8 in range(10):
                                                            if combination.count(str(digit8)) == 0:
                                                                combination += str(digit8)
                                                                for digit9 in range(10):
                                                                    if combination.count(str(digit9)) == 0:
                                                                        combination += str(digit9)
                                                                        for digit10 in range(10):
                                                                            if combination.count(str(digit10)) != 0:
                                                                                continue
                                                                            combination += str(digit10)
                                                                            combinations.append(combination)
                                                                            print(combination)
                                                                            if len(combinations) == 1000000:
                                                                                print(combinations[-1])
                                                                                return


def solve3():
    x = 0
    for i in range(int(math.pow(10,10))):
        if i % 7 == 0:
            x += 1
    print("done")


solve3() """



