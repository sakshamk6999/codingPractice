from collections import defaultdict
n, k = map(int, input().split())
a = list(map(int, input().split()))
s = list(set(a))
p = len(s)
rec = defaultdict(int)
for i in range(p):
    rec[s[i]] = 0

m = []
start = 0
l = 0

for i in a:
    # print(m)
    if rec[i] == 0 and l < k:
        rec[i] = 1
        l += 1
        m.append(i)
    elif rec[i] == 0 and l == k:
        rec[a[start]] = 0
        m.append(i)
        rec[i] = 1
        start += 1

print(len(m) - start)
for i in range(len(m) - 1, start - 1, - 1):
    print(m[i], end=' ')








