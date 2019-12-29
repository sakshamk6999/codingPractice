from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    record = defaultdict(list)
    for i in range(n):
        record[a[i]].append(i)
    t = sorted(a)
    l, r = 0, 0
    star = 0
    for i in range(n - 1):
        tStar = 0
        r = t[n - 1] // t[i]
        l = t[i + 1] // t[i]
        p = record[t[i]].pop()
        for j in range(l, r + 1):
            if record.get(t[i]*j, 0) != 0:
                for k in record[t[i] * j]:
                    if k < p:
                        tStar += 1
        star = max(tStar, star)

    print(star)