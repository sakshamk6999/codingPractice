from math import ceil
for _ in range(int(input())):
    n, d = map(int, input().split())
    if n//2 + ceil(d/((n//2) + 1)) <= n:
        print('YES')
    else:
        print('NO')