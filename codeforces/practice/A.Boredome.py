n = int(input())
a = sorted(list(map(int, input().split())))
rec = {}

for i in a:
    rec[i] = rec.get(i, 0) + 1

k = sorted(rec.keys()).copy()
na = len(k)
dp = [0 for i in range(na)]
for i in range(na):
