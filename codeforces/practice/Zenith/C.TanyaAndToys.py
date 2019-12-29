n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
t = 0
ans = []
i = 0
p = 1
while m > 0:
    if i < n and a[i] == p:
        i += 1
    else:
        if m >= p:
            m -= p
            t += 1
            ans.append(p)
        else:
            break
    p += 1

print(t)
for i in ans:
    print(i, end=' ')