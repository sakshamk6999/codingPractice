from collections import defaultdict
for _ in range(int(input())):
    a1, a2, a3, c1, c2, c3 = map(int, input().split())
    flag = 1
    record = {}
    record = defaultdict(lambda : -1, record)
    if record[a1] == -1:
        record[a1] = c1
    else:
        if c1 != record[a1]:
            flag = 0

    if record[a2] == -1:
        record[a2] = c2
    else:
        if c2 != record[a2]:
            flag = 0

    if record[a3] == -1:
        record[a3] = c3
    else:
        if c3 != record[a3]:
            flag = 0

    if flag == 0:
        print('NOT FAIR')

    else:
        l = sorted([a1, a2, a3])
        if ((l[0] != l[1] and record[l[0]] < record[l[1]]) or (l[1] == l[0] and record[l[0]] == record[l[1]])) and ((l[1] != l[2] and record[l[1]] < record[l[2]]) or (l[1] == l[2] and record[l[1]] == record[l[2]])):
            print('FAIR')
        else:
            print('NOT FAIR')