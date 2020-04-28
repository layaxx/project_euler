""" begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file? """


def solve():
    file = open("022_names.txt")

    if file.mode == 'r':
        contents = file.read()
        contents = contents[1:]
        contents = contents[:len(contents) - 1]
        allLines = contents.split("\",\"")
        allLines.sort()
    else:
        print("Error - couldnt open file")

    sum = 0

    for line in allLines:
        sum += value(line) * (allLines.index(line) + 1)
    print(sum)


def value(string):
    value = 0
    for char in string:
        value += 1 + ord(char) - ord("A")
    return value


solve()
