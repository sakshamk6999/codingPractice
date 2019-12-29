n = int(input())
a = sorted(list(map(int, input().split())))
d = {}
ans = 0
de = []
for i in range(n):
    if d.get(a[i], 0) == 0:
        d[2*a[i]] = 1
    else:
        ans += 1
        de.append(a[i])
print(ans)
for i in de:
    print(i)