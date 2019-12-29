n = int(input())
s = list(input())
t = list(input())
s1 = []
l1 = 0
s2 = []
l2 = 0
for i in range(n):
    if s[i] != t[i]:
        if s[i] == 'a':
            s1.append(i + 1)
            l1 += 1
        else:
            s2.append(i + 1)
            l2 += 1

if l1 % 2 == l2 % 2:
    ans = []
    ansL = 0
    for i in range(0, l1 - 1, 2):
        ans.append([s1[i], s1[i + 1]])
        ansL += 1

    for i in range(0, l2 - 1, 2):
        ans.append([s2[i], s2[i + 1]])
        ansL += 1

    if l1 % 2 != 0:
        ansL += 2
        ans.append([s1[l1 - 1], s1[l1 - 1]])
        ans.append([s1[l1 - 1], s2[l2 - 1]])
    print(ansL)
    for i in ans:
        print(i[0], i[1])
else:
    print(-1)
