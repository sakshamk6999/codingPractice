import math
from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    rec = defaultdict(list)
    ans = 0
    temp = [0 for i in range(n)]
    rec[a[n - 1]].append(n - 1)
    for i in range(n - 2, -1, -1):
        j = 1
        while j <= math.sqrt(a[i]):
            if a[i] % j == 0:
                if int(a[i] / j) == j:
                    if rec.get(j, 0) != 0:
                        for k in rec[j]:
                            temp[k] += 1
                else:
                    if rec.get(j, 0) != 0:
                        for k in rec[j]:
                            temp[k] += 1
                    if rec.get(int(a[i]/j), 0) != 0:
                        for k in rec[int(a[i]/j)]:
                            temp[k] += 1
            j += 1
        rec[a[i]].append(i)

    # print(temp)
    print(max(temp))