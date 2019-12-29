from collections import defaultdict

n, q = map(int, input().split())
graph = defaultdict(list)
mat = [[0 for i in range(n)]for i in range(q)]

for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

initial = list(map(int, input().split()))
for t in range(1, q + 1):
    query = input().split()
    if query[0] == '+':
        continue
    else:
        print(0)

