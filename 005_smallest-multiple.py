
def solve():
    print("working")
    n = 20;
    while not correct(n):
        n += 20

    print(str(n))


def correct(num):
    for x in range(11, 21):
        if not num % x == 0:
            return False
    return True

solve()