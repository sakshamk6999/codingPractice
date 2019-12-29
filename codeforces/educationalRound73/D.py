n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
vis = [0 for i in range(len(a))]
c = []
d = {}
for i in range(len(a)):
    if a[i] in d:
        d[a[i]].append(i)
    else:
        d[a[i]] = [i]
ans = 0
for i in d.keys():
    if len(d[i]) >= 2:
        for j in d[i]:
            ans += b[j]
            vis[j] = 1
            c.append(a[j])
c = set(c)
for i in range(len(a)):
    if vis[i] == 0:
        for j in c:
            if (j > a[i]) and (j&a[i] == a[i]):
                c.add(a[i])
                ans += b[i]
                break
print(ans)

