from collections import defaultdict

rec = defaultdict(list)
for _ in range(int(input())):
    a, b = map(int, input().split())
    rec[a].append(b)

ans = 0
for i in sorted(rec.keys()):
    for j in sorted(rec[i]):
        if ans <= j:
            ans = j
        else:
            ans = i

print(ans)