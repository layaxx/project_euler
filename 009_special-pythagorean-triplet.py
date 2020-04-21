# a + b + c = 1000 | a*a + b*b = c*c | a*b*c

def solve():
    for a in range(1, 999):
        for b in range(1, 999):
            for c in range(1, 999):
                if (a*a) + (b*b) == (c*c):
                    if a + b + c == 1000:
                        print(a*b*c)


solve()