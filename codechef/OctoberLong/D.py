from collections import defaultdict
l = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
n = int(input())
graph = defaultdict(list)
rec = {}
rec = defaultdict(lambda : 0, rec)
price = []
for i in range(3):
    price.append(list(map(int, input().split())))
flag = 0
for i in range(n - 1):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)
    rec[u - 1] += 1
    rec[v - 1] += 1
    if rec[u - 1] >= 3 or rec[v - 1] >= 3:
        flag = 1

if flag == 1:
    print(-1)
else:
    path = []
    start = 1
    for i in range(n):
        if rec[i] == 1:
            start = i
            break
    q = [start]
    prev = start
    while q != []:
        t = q.pop(0)
        path.append(t)
        for i in graph[t]:
            if prev != i:
                q.append(i)
        prev = t

    ans = float('inf')
    ansL = 0
    for i in range(6):
        l[i] = l[i] * (n//3) + l[i][:n % 3]
        temp = 0
        for j in range(n):
            temp += price[l[i][j] - 1][path[j]]
        ans = min(temp, ans)
        if ans == temp:
            ansL = i

    print(ans)
    for i in l[ansL]:
        print(i, end=' ')
    print('')