from collections import defaultdict
n, k = map(int, input().split())
record = defaultdict(list)
numL = defaultdict(int)
numR = defaultdict(int)
position = defaultdict(list)
minL = float('inf')
maxR = 0

for i in range(n):
    l, r = map(int, input().split())
    minL = min(minL, l)
    maxR = max(maxR, r)
    record[l].append(r)
    position[(l, r)].append(i + 1)
    if numL.get(l, 0) == 0:
        numL[l] = 1
    else:
        numL[l] += 1

    if numR.get(r, 0) == 0:
        numR[r] = 1
    else:
        numR[r] += 1

for i in record.keys():
    record[i].sort()

ans = []
m = 0
temp = 0

for i in range(minL, maxR + 1):
    if numL.get(i, 0) != 0:
        temp += numL[i]
        while temp > k:
            tempR = record[i].pop()
            ans.append(position[(i, tempR)].pop())
            if numR.get(tempR, 0) != 0:
                numR[tempR] -= 1
            temp -= 1
            m += 1
    temp -= numR.get(i, 0)

print(m)
for i in ans:
    print(i, end=' ')
print('')
