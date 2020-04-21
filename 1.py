output = 0
for x in range(1,1000):
    if x % 5 == 0 or x % 3 == 0:
        output += x
print(output)