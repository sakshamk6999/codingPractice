from collections import defaultdict

for _ in range(int(input())):
    n, m = map(int, input().split())
    record = {}
    record = defaultdict(lambda : 0, record)
    graph = defaultdict(list)
    for i in range(m):
        u, v = map(int, input().split())
        record[u] += 1
        record[v] += 1
        graph[u].append(v)
        graph[v].append(u)

    if m % 2 == 0:
        print(1)
        for i in range(n):
            print(1, end=' ')
        print('')
    else:
        vertices = [1 for i in range(n)]
        flag = 0
        for i in range(1, n + 1):
            if record[i] % 2 != 0:
                vertices[i - 1] = 2
                flag = 1
                break
        if flag == 0:
            # vertices[0] = 2
            # vertices[graph[1].pop() - 1] = 3
            for i in range(1, n + 1):
                if record[i] > 0:
                    vertices[i - 1] = 2
                    vertices[graph[i].pop() - 1] = 3
                    break
            print(3)
        else:
            print(2)
        for i in vertices:
            print(i, end=' ')
        print('')