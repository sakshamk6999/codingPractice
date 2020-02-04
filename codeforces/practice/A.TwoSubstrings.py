s = list(input())
ab = 0
ba = 0
aba = 0
bab = 0
flag = 0
n = len(s)
i = 1
while i < n:
    if ab == 0 and s[i] == 'A' and s[i - 1] == 'B':
        ab += 1
        i += 2
        continue
    if ab > 0 and s[i] == 'B' and s[i - 1] == 'A':
        ba += 1
        break
    i += 1
flag = 1 if ab > 0 and ba > 0 else 0
if flag == 0:
    i = 1
    ab = 0
    ba = 0
    while i < n:
        if ab == 0 and s[i] == 'B' and s[i - 1] == 'A':
            ab += 1
            i += 2
            continue
        if ab > 0 and s[i] == 'A' and s[i - 1] == 'B':
            ba += 1
            break
        i += 1
    flag = 1 if ab > 0 and ba > 0 else 0
if flag == 1:
    print('YES')
else:
    print('NO')