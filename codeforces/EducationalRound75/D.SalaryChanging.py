from collections import defaultdict
for _ in range(int(input())):
    n, s = map(int, input().split())
    record = defaultdict(list)
    for i in range(n):
        l, r = map(int, input().split())
        record[l].append(r)

    for i in record.keys():
        record[i].sort()

    sal = []
    up = []
    for i in sorted(record.keys()):
        for j in record[i]:
            sal.append(i)
            up.append(j)

    remaining = s - sum(sal)
    e = 1
    ans = sal[n//2]
    for i in range(n//2 + 1, n):
        if remaining >= e * (sal[i] - sal[i - 1]) and up[n//2]:
            remaining -= e * (sal[i] - sal[i - 1])
            e += 1
            ans = sal[i]
        else:
            break

    print(ans)

