n = int(input())
a = list(map(int, input()))
b = list(map(int, input()))
diff = []
i = 0
ans = 0
while i < n:
    if a[i] != b[i]:
        if i + 1 < n and a[i + 1] != b[i + 1] and a[i] != a[i + 1]:
            i += 2
        else:
            i += 1
        ans += 1
    else:
        i += 1
print(ans)
