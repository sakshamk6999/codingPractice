from collections import defaultdict
import heapq

n, k = map(int, input().split())

postition = defaultdict(list)
right = defaultdict(list)
postitionR = defaultdict(list)
minL = float('inf')
maxR = 0
numL = defaultdict(int)
numR = defaultdict(int)
for i in range(1, n + 1):
    l, r = map(int, input().split())
    postition[(l, r)].append(i)
    right[r].append(l)
    postitionR[l].append(r)
    minL = min(minL, l)
    maxR = max(maxR, r)
    if numL.get(l, 0) == 0:
        numL[l] = 1
    else:
        numL[l] += 1

    if numR.get(r, 0) == 0:
        numR[r] = 1
    else:
        numR[r] += 1

temp = 0
heap = []
ans = []
m = 0
for i in range(minL, maxR + 1):
    if numL.get(i, 0) != 0:
        temp += numL[i]
        for j in range(numL[i]):
            heapq.heappush(heap, -1 * postitionR[i].pop())

        while temp > k:
            t = -1 * heapq.heappop(heap)
            if numR.get(t, 0) != 0:
                numR[t] -= 1
            temp -= 1
            m += 1
            ans.append(postition[(right[t].pop(), t)].pop())
    temp -= numR.get(i, 0)
print(m)
for i in ans:
    print(i, end=' ')

print('')
