from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    graph = defaultdict(list)
    for i in range(n):
        x, y = map(int, input().split())
        graph[y].append(x)

    x = 0
    y = 0
    ans = []
    flag = 1
    for i in sorted(graph.keys()):
        for j in sorted(graph[i]):
            if y > i or x > j:
                flag = 0
                break
            else:
                ans.append('R' * (j - x))
                ans.append('U' * (i - y))
                x = j
                y = i
        if flag == 0:
            break
    if flag == 0:
        print('NO')
    else:
        print('YES')
        print(''.join(ans))