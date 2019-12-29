from math import ceil
for _ in range(int(input())):
    n, m, e = map(int, input().split())
    if (n + e - m) < 0:
        print(0)
    else:
        print(ceil((n + e - m)/2))
