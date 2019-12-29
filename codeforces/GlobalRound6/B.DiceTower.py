n = int(input())
a = list(map(int, input().split()))
s = [i for i in range(15, 21)]
# print(s)
for i in a:
    flag = 0
    for t in s:
        if i >= t and (i - t) % 14 == 0:
            flag = 1
            break
    if flag:
        print('YES')
    else:
        print('NO')