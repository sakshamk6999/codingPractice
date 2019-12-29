from collections import defaultdict
import queue
def compare(record, s, n):
    temp = record[s].copy()
    value = {}
    value = defaultdict(int)
    graph = defaultdict(list)
    for i in range(n):
        value[i] = 0
    value[0] = 1
    for i in range(n):
        for j in range(i + 1, n):
            #if instersecting
            if (temp[i][0] <= temp[j][1] and temp[i][0] >= temp[j][0])or (temp[i][1] >= temp[j][0] and temp[i][1] <= temp[j][1]):
                graph[i].append(j)
                graph[j].append(i)
    q = queue.Queue()
    q.put(0)
    flag = 1
    visited = [0 for i in range(n)]
    while not q.empty():
        t = q.get()
        visited[t] = 1
        for i in graph[t]:
            if visited[i] == 0:
                if value[i] == value[t]:
                    flag = 0
                    break
                else:
                    if value[i] == 0:
                        value[i] = -1 * value[t]
                        q.put(i)
        if flag == 0:
            break
    return flag


for _ in range(int(input())):
    n = int(input())
    length = {}
    length = defaultdict(lambda : 0, length)
    record = defaultdict(list)
    for i in range(n):
        u, v, w = map(int, input().split())
        record[w].append([u, v])
        length[w] += 1

    flag = 1
    for i in record.keys():
        if compare(record, i, length[i]) == 0:
            flag = 0
            break

    if flag == 0:
        print('NO')
    else:
        print('YES')

