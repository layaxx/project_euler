# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?


def generateSpiral(number):
    if number % 2 == 0:
        print("Spiral dimensions must be odd. has been adjusted by +1")
        number += 1

    spiral = []

    for i in range(number):
        l1 = []
        for j in range(number):
            l1.append(0)
        spiral.append(l1)

    

    spiral[int(number/2)][int(number/2)] = 1

    count = 2

    index = [int(number/2), int(number/2) + 1]

    length = 1
    for turn in range(int(number / 2)):
        # index = down(index, 1)
        for i in range(length):
            spiral[index[0]][index[1]] = count
            count += 1
            index[0] += 1 

        #index = left(index, 2)
        length += 1
        for i in range(length):
            spiral[index[0]][index[1]] = count
            count += 1
            index[1] -= 1 


        #index = up(index, 2)
        for i in range(length):
            spiral[index[0]][index[1]] = count
            count += 1
            index[0] -= 1 

        #index = right(index, 3)
        length += 1
        for i in range(length):
            spiral[index[0]][index[1]] = count
            count += 1
            index[1] += 1 

    return spiral



def printArray(spiral):
    for row in spiral:
        for value in row:
            if len(str(value)) == 1:
                value = "0" + str(value)
            print(str(value) + " ", end="")
        print()

def solve(n):
    spiral = generateSpiral(n)

    sum = 0
    for x in range(n):
        sum += spiral[x][x]
        sum += spiral[x][n - 1 - x]

    # Field in Middle is counted twice, solved by subtracting 1 since Field in middle is 1 by definition    
    sum -= 1

    print(sum)


solve(1001)


