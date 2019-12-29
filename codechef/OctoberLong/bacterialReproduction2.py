from collections import defaultdict
import queue
#
# def doDfs(n, parent, graph, temp, path, length):
#     temp.append(n)
#     for i in graph[n]:
#         if i != parent[n]:
#             path[i] = [length]
#             path[i].append(temp.copy())
#             parent[i] = n
#             doDfs(i, parent, graph, temp, path, length + 1)
#     temp.pop()
#     return

def Bfs(graph, path, n, height, leaf):
    q = queue.Queue()
    q.put([1, 0, []])
    visited = [0 for i in range(n + 1)]
    while not q.empty():
        u, l, temp = q.get()
        visited[u] = 1
        # path[u] = [l]
        # path[u].append(temp.copy())
        path[u] = temp.copy()
        flag = 0
        for i in graph[u]:
            if visited[i] == 0:
                flag = 1
                height[i] = height[u] + 1
                q.put([i, l + 1, temp + [u]])
        if flag == 0:
            leaf[u] = 1

n, q = map(int, input().split())
graph = defaultdict(list)

for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

initial = list(map(int, input().split()))

record = defaultdict(int)

parent = [-1 for i in range(n + 1)]
# temp = []
path = [[] for i in range(n + 1)]
height = [0 for i in range(n + 1)]
leaf = [0 for i in range(n + 1)]
# doDfs(1, parent, graph, temp, path, 1)
Bfs(graph, path, n, height, leaf)
# print(path)

for i in range(1, q + 1):
    l = input().split()
    u = int(l[1])
    # print(record)
    if l[0] == '?':

        ans = 0
        if leaf[u]:
            ans = initial[u - 1]
        if i >= height[u]:
            for j in range(height[u]):
                # print((path[u][j], i - height[u] + j))
                ans += record.get((path[u][j], i - height[u] + j), 0)
                ans += record.get((u, i - height[u] + j), 0)
                if leaf[u]:
                    ans += initial[path[u][j] - 1]
                    for k in range(1, i - height[u] + j):
                        ans += record.get((path[u][j], k), 0)
                        ans += record.get((u, k), 0)
        else:
            time = 1
            for j in range(height[u] - i, height[u]):
                ans += initial[path[u][j] - 1] + record.get((path[u][j], time), 0)
                ans += record.get((u, time), 0)
                if leaf[u]:
                    for k in range(1, time):
                        ans += record.get((path[u][j], k), 0)
                        ans += record.get((u, k), 0)
                time += 1
        print(ans)
    else:
        record[u, i] = int(l[2])


