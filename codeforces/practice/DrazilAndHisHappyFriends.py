n, m = map(int, input().split())
boy = list(map(int, input().split()))
girl = list(map(int, input().split()))
b = [0 for i in range(n)]
g = [0 for i in range(m)]

for i in range(1, boy[0] + 1):
    b[boy[i]] = 1

for i in range(1, girl[0] + 1):
    g[girl[i]] = 1

rec = {}
lb = boy[0]
lg = girl[0]
i = 0
flag = 1
for i in range(n):
    for j in range(m):
        if b[i] == 1 and g[j] == 0:
            g[j] = 1
            lg += 1
        elif g[j] == 1 and b[i] == 0:
            b[i] = 1
            lb += 1
        if lg == m and lb == n:
            break

    if lg == m and lb == n:
        break

if lb == n and lg == m:
    print('Yes')
else:
    print('No')