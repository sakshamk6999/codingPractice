import math
from collections import defaultdict
def divisors(n, ans):
    i = 2
    while i <= math.sqrt(n):

        if (n % i == 0):
            if (n / i == i):
                ans.append(i)
            else:
                ans.append(i)
                ans.append(n // i)
        i = i + 1

for _ in range(int(input())):
    n = int(input())
    d1 = []
    # d2 = []
    divisors(n, d1)
    rec = defaultdict(int)
    for i in d1:
        rec[i] = 1
    flag = 0

    for i in d1:
        d2 = []
        divisors(n//i, d2)
        for j in d2:
            if rec.get(j, 0) != 0 and rec.get((n//i)//j, 0) != 0 and (n//i)//j != j and (n//i)//j != i and i != j:
                flag = 1
                print('YES')
                print(i, j, (n//i)//j)
                break
        if flag == 1:
            break
    if flag == 0:
        print('NO')