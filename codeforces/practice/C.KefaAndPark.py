from collections import defaultdict

ans = 0
def dfs(v, k, visit, m, graph, isRed):
    global ans
    visit[v] = 1
    temp = 0
    if k > m:
        # print(v)
        return

    for i in graph[v]:
        temp += 1
        if visit[i] == 0:
            dfs(i, (k + 1)*isRed[i], visit, m, graph, isRed)
    if temp == 1 and v != 1:
        ans += 1
        # print(ans)

n, m = map(int, input().split())
graph = defaultdict(list)
isRed = [0 for i in range(n + 1)]
a = list(map(int, input().split()))
for i in range(n):
    isRed[i + 1] = a[i]
for _  in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [0 for i in range(n + 1)]
dfs(1, isRed[1], visit, m, graph, isRed)
print(ans)