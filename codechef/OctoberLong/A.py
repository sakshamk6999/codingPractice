from math import ceil
for _ in range(int(input())):
    a, b, c, d, k = map(int, input().split())
    x = ceil(a/c)
    y = ceil(b/d)
    if x + y <= k:
        print(x, y)
    else:
        print(-1)