from collections import defaultdict
n = int(input())
rec = {}
rec = defaultdict(lambda : 0, rec)
a = input().split()
b = input().split()
a1 = 0
b1 = 0
ans = 0
while a1 < n and b1 < n:
    if rec[a[a1]] != 0:
        a1 += 1

    elif a[a1] == b[b1]:
        rec[a[a1]] += 1
        a1 += 1
        b1 += 1

    else:
        ans += 1
        rec[b[b1]] += 1
        b1 += 1

print(ans)
