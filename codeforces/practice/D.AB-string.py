n = int(input())
s = list(input())

p = [[0 for i in range(n)]for i in range(n)]
l = [0 for i in range(n)]
dp = [[0 for i in range(n)]for i in range(n)]
r = [0 for i in range(n)]

for i in range(n):
    p[i][i] = 1

for diff in range(1, n):
    for i in range(n):
        j = i + diff
        if diff == 1:
            if s[i] == s[j]:
                p[i][j] = 1
                l[i] = j
                r[j] = i
        else:
            if s[i] == s[j] and p[i + 1][j - 1] == 1:
                p[i][j] = 1
                if l[i] == 0:
                    l[i] = 1
                if l[j] == 0:
                    l[j] = 1

