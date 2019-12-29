from collections import defaultdict
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    record = defaultdict(int)
    for i in range(1, n + 1):
        record[i] = 1
    l = []
    i = 0
    temp = []
    tl = 0
    while i < n:
        if a[i] == -1:
            temp.append(-1)
            i += 1
            tl += 1
        else:
            temp.append(a[i])
            l.append([temp, tl + 1])
            tl = 1
            temp = [a[i]]
            i += 1
    if a[n - 1] == -1:
        l.append([temp, tl])

    for i in l:
        nTemp = i[1]
        tempList = i[0]
        if tempList[0] != -1:
            record[tempList[0]] = 0
        if tempList[0] != -1:
            record[tempList[nTemp - 1]] = 0
        initial = -1
        later = -1
        for i in range(1, tempList[0]):
            if record[i] == 1:
                initial = i
                record[i] = 0
                break
        if initial == -1:
            for i in range(tempList[0] + 1, k + 1):
                if record[i] == 1:
                    initial = i
                    record[i] = 0
                    break

        for i in range(1, tempList[0]):
            if record[i] == 1:
                later = i
                record[i] = 0
                break
        if later == -1:
            for i in range(tempList[0] + 1, k + 1):
                if record[i] == 1:
                    later = i
                    record[i] = 0
                    break
        if later == -1:

        for j in range(nTemp):



