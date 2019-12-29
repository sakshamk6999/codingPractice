from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    record = {}
    record = defaultdict(lambda : 0, record)
    ans = 0
    record[a[0]] = 1
    minMax = [[] for i in range(n)]
    minMax[0] = [a[0], a[0]]
    for i in range(1, n):
        record[a[i]] += 1
        minMax[i] = [min(minMax[i - 1][0], a[i]), max(minMax[i - 1][1], a[i])]
    # print(minMax)
    for i in range(n - 1, 0, -1):
        if i <= ans:
            break
        record[a[i]] -= 1
        # print(record)
        flag = 0
        l = minMax[i - 1][0]//a[i]
        r = minMax[i - 1][1]//a[i]
        if r - l + 1 > i:
            flag = 1
        temp = 0
        if flag == 0:
            for j in range(l, r + 1):
                temp += record[a[i]*j]
        else:
            for j in range(i):
                if a[j] % a[i] == 0:
                    temp += 1
        ans = max(ans, temp)
    print(ans)