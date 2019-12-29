n = int(input())
a = sorted(list(map(int, input().split())))
l = 0
ans = 0
flag = 0
for i in range(n):
    if a[i] < 0:
        ans += (-1*a[i]) - 1
    else:
        if flag == 0:
            l = i
            flag = 1
        if a[i] == 0:
            ans += 1
        else:
            ans += a[i] - 1

if l % 2 != 0:
    ans += 2

print(ans)
