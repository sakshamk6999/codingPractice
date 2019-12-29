from collections import defaultdict

d = {}
d = defaultdict(lambda : 0, d)
val = {}
val = defaultdict(lambda : -1, val)

def findVal(v, t, d, val, parent, graph):
    if val[v, t] != -1:
        return val[v, t]
    if v == 1:
        return d[1, t]
    if graph[v] == [parent[v]]:
        val[v, t] = d[v, t] + findVal(parent[v], t - 1, d, val, parent, graph) + findVal(v, t - 1, d, val, parent, graph)
        return val[v, t]
    val[v, t] = d[v, t] + findVal(parent[v], t - 1, d, val, parent, graph)
    return val[v, t]

def doDfs(n, parent, graph):
    for i in graph[n]:
        if i != parent[n]:
            parent[i] = n
            doDfs(i, parent, graph)
    return

n, q = map(int, input().split())
graph = defaultdict(list)

for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


initial = list(map(int, input().split()))
parent = [-1 for i in range(n + 1)]
doDfs(1, parent, graph)
# print(parent)

for i in range(1, n + 1):
    d[i, 0] = initial[i - 1]
    val[i, 0] = initial[i - 1]

for t in range(1, q + 1):
    query = input().split()
    v = int(query[1])
    if query[0] == '+':
        d[v, t] = int(query[2])
    else:
        print(findVal(v, t, d, val, parent, graph))