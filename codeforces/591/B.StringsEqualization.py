for _ in range(int(input())):
    s1 = list(input())
    s2 = list(input())
    r = {}
    for i in s1:
        r[i] = 1
    flag = 0
    for i in s2:
        if r.get(i, 0) != 0:
            flag = 1
            break
    if flag:
        print('YES')
    else:
        print('NO')