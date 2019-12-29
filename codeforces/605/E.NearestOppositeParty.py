import queue
from collections import defaultdict

def bfs(src1, src2, n, graph, ans):
    d = [float('inf') for i in range(n)]
    q = queue.Queue()
    for i in src1:
        d[i] = 0
        q.put(i)

    while not q.empty():
        v = q.get()
        for i in graph[v]:
            if d[i] == float('inf'):
                d[i] = d[v] + 1
                q.put(i)

    for i in src2:
        if d[i] != float('inf'):
            ans[i] = d[i]

n = int(input())
s = list(map(int, input().split()))
graph = defaultdict(list)
odd = []
even = []
for i in range(n):
    l = i - s[i]
    r = i + s[i]
    if l >= 0:
        graph[l].append(i)
    if r < n:
        graph[r].append(i)
    if s[i] % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

ans = [-1 for i in range(n)]

bfs(even, odd, n, graph, ans)
bfs(odd, even, n, graph, ans)

for i in ans:
    print(i, end=' ')

print('')