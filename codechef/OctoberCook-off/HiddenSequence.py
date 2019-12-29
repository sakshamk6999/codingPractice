import queue
from collections import defaultdict
for _ in range(int(input())):
    n, k, m = map(int, input().split())
    ans = [0 for i in range(n)]
    q = []
    record = {}
    record = defaultdict(lambda : 0, record)
    change = defaultdict(list)

    for i in range(m):
        q.append(list(map(int, input().split())))

    q.sort(key=lambda x: x[2])
    start = 0
    # fill = 0
    flag = 1
    for i in range(m):
        x, y, z = q[i][0], q[i][1], q[i][2]
        z -= 1
        diff = y - 1 - record[x]
        record[x] += diff + 1
        ans[z] = x
        if z - start < diff:
            flag = 0
            break
        else:
            p = 0
            j = 0
            change[z] = [x, diff]
            # while j < diff:
            #     if ans[start + p] == 0:
            #         ans[start + p] = x
            #         j += 1
            #     p += 1
    i = n - 1
    print(change)
    for i in range(n - 1, q[m - 1][2] - 1, -1):
        ans[i] = 1
    # print(i)
    q = queue.Queue()
    q.put()
    while i >= 0:
        # print(i)
        if change.get(i, []) == []:
            if i >= q[m - 1][2]:
                ans[i] = 1
                i -= 1
            else:
                flag = 0
                break
        else:
            x, diff = change[i]
            for j in range(diff + 1):
                ans[i - diff] = x
            i -= (diff + 1)
    # for i in range(q[m - 1][2]):
    #     #     if ans[i] == 0:
    #     #         flag = 0
    #     #         break
    if flag == 0:
        print('No')
    else:
        print('Yes')
        for i in range(n):
            if ans[i] == 0:
                print(1, end=' ')
            else:
                print(ans[i], end=' ')
        print('')