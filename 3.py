num = 600851475143

div = 2 
while num != 1:
    while num % div == 0:
        num = num / div  
    div = div + 1

print(div - 1)  