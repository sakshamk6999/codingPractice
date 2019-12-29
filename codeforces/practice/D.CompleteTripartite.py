from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
for i in range(m):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
total = set()
for i in range(n):
    total.add(i)

for i in graph[0]:
    total.remove(i)
color = [0 for i in range(n)]
color[0] = 1

for i in total:
    color[i] = 1

for i in color:
