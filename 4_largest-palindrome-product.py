# largest palindrom made from multiplikation of two 3-digit numbers

def solution():
    num1 = num2 = 999
    results = []
    while num1 > 99:
        while num2 > 99:
            if isPalindrom(num1*num2):
               results.append(num1*num2)
            num2 = num2 - 1
        num1 = num1 - 1
        num2 = 999
    results.sort(reverse=True)
    print(results[0])

def isPalindrom(n):
    string = str(n)
    for x in range(0, int(len(string)/2)):
        if string[x] != string[len(string) - 1 - x]:
            return False    
    return True


solution()