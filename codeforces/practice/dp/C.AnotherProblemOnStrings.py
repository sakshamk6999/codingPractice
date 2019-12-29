k = int(input())
a = list(map(int, list(input())))
s = []
n = len(a)
l = 0
for i in range(n):
    if a[i] == 1:
        s.append(i)
        l += 1

if l < k:
    print(0)
else:
    ans = 0
    if k + 1 < l:
        ans = s[k + 1] - s[k]
    else:
        ans = l - s[k]

    for i in range(k + 1, l):
        if i + 1 < l:
            ans += (s[i - k] - s[i - k - 1])*(s[i + 1] - s[i])
        else:
            ans += (s[i - k] - s[i - k - 1])*(l - s[i])

    print(ans)
