# sum of even fibonnaci numbers <= 4 000 000

fib = [1, 2]
new = 3
i = 2
while (not new > 4000000):
    fib.append(new)
    new = fib[i] + fib[i-1]
    i = i + 1
output = 0
for x in fib:
    if x % 2 == 0:
        output += x

print(output)
