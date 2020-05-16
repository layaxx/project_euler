

def solve():
    sum = 0
    for number in range(0, 8000):
        if test(number):
            continue
        l = getAllTeiler(number)

        for entry in l:
            if check(entry, number):
                print(entry)
                print(number)
                print("--------")
                sum += number
                break

    print(sum)

def test(number):
    array = [0,0,0,0,0,0,0,0,0,0]
    for digit in str(number):
        if digit == 0:
            return True
        if array[int(digit)] != 0:
            return True
        array[int(digit)] += 1
    return False

def check(mults, number):
    n = "" + str(number) + str(mults[0]) + str(mults[1])

    
    if(len(n) != 9):
        return False

    array = [0,0,0,0,0,0,0,0,0,0]
    for digit in n:
        array[int(digit)] += 1

    if array[0] != 0:
        return False

    for i in range(1, 10):
        if array[i] != 1:
            return False

    return True


def getAllTeiler(number):
    l = []

    for i in range(1, int(number / 2) + 2):
        if int(number / i) * i == number:
            l.append((i, int(number/i)))
    return l

        

solve()

# print(check((39, 186), 7254))