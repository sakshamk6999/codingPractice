import math
for _ in range(int(input())):
    x, y = map(int, input().split())
    n, m, k = map(int, input().split())

    temp = list(map(int, input().split()))
    distance = 0
    tempMin = float('inf')
    print(x, y)
    for i in range(0, 2*n, 2):
        t = min(tempMin, math.sqrt(((x - temp[i]) ** 2) + ((y - temp[i + 1]) ** 2)))
        if tempMin == t:
            X = temp[i]
            Y = temp[i + 1]
        tempMin = t
    distance += tempMin

    x = X
    y = Y
    print(x, y)
    temp = list(map(int, input().split()))
    tempMin = float('inf')
    for i in range(0, 2 * m, 2):
        t = min(tempMin, math.sqrt(((x - temp[i]) ** 2) + ((y - temp[i + 1]) ** 2)))
        if tempMin == t:
            X = temp[i]
            Y = temp[i + 1]
        tempMin = t

    x = X
    y = Y
    print(x, y)
    distance += tempMin
    tempMin = float('inf')
    temp = list(map(int, input().split()))
    for i in range(0, 2 * k, 2):
        t = min(tempMin, math.sqrt(((x - temp[i]) ** 2) + ((y - temp[i + 1]) ** 2)))
        if tempMin == t:
            X = temp[i]
            Y = temp[i + 1]
        tempMin = t
    distance += tempMin
    x = X
    y = Y
    print(x, y)
    print(distance)
