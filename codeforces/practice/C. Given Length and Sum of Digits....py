m, s = map(int, input().split())

ma = [0 for i in range(m)]
mi = [0 for i in range(m)]
temp = s
flag = 0
j = 0
for i in range(m - 1, -1, -1):
    # if temp < 0 or s < 0:
    #     flag = 1
    #     break
    mi[i] = min(temp - i, 9)
    # print(j, "s", s)
    ma[j] = min(9, s - (m - j - 1))
    temp -= mi[i]
    s -= ma[j]
    if ma[j] < 0 or mi[i] < 0:
        flag = 1
        break
    j += 1

if flag:
    print("-1 -1")
else:
    for i in mi:
        print(i, end='')
    print(end=' ')
    for i in ma:
        print(i, end='')
    print('')