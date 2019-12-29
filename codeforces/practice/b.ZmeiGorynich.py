from math import ceil
for _ in range(int(input())):
    n, k = map(int, input().split())
    attacks = []
    temp = []
    for i in range(n):
        t1, t2 = map(int, input().split())
        attacks.append([t1, t2])
        temp.append(t1)
    attacks.sort(key=lambda x: x[0] - x[1])
    temp.sort()
    step = 0
    if attacks[n - 1][0] - attacks[n - 1][1] < 0:
        print(-1)
        continue
    step = ceil(temp[n - 1] - k)//(attacks[n - 1][1] - attacks[n - 1][0])
    print(step + 1)