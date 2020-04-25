
limit = 20
cache = []

def initialiseCache():
    global cache
    for x in range(limit):
        tmp = []
        for y in range(limit):
            tmp.append(-1)
        cache.append(tmp)


def findPathsFrom(position):
    if position[0] == limit or position[1] == limit:
        return 1
    
    if cache[position[0]][position[1]] == -1:
        cache[position[0]][position[1]] = findPathsFrom((position[0] + 1, position[1])) + findPathsFrom((position[0], position[1] + 1))
    
    return cache[position[0]][position[1]]


def solve():
    initialiseCache()
    print(findPathsFrom((0,0)))

solve()


