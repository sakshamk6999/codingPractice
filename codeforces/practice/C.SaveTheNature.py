def ans(p, n, a, b, x, y):
    countX, countY, countXY = 0, 0, 0
    ans = 0
    for i in range(1, n):
        if i % a == 0 and i % b == 0:
            countXY += 1
        elif i % a == 0:
            countX += 1
        elif i % b == 0:
            countY += 1
    for i in range(countXY):
        ans += p[i] * (x + y)
    for i in range(countX):
        ans += p[i + countXY] * x
    for i in range(countY):
        ans += p[i + countXY + countX] * y
    return ans

for _ in range(int(input())):
    n = int(input())
    p = sorted(list(map(int, input().split())), reverse=True)
    x, a = map(int, input().split())
    y, b = map(int, input().split())
    k = int(input())
    if x < y:
        x, y = y, x
        a, b = b, a

    l = 0
    r = n + 1
    while r - l > 1:
        m = (l + r)//2
        if ans(p, m, a, b, x, y) >= k:
            r = m
        else:
            l = m

    if r > n:
        r = -1

    print(r)
