n = int(input())
a = list(map(int, input().split()))
gotGifts = {}
rem = []
for i in range(n):
    if a[i] != 0:
        gotGifts[a[i]] = 1
    else:
        rem.append(i + 1)
# n = len(a)
left = []
l = 0
for i in range(1, n + 1):
    if gotGifts.get(i, 0) == 0:
        left.append(i)
        l += 1

j = 0
for i in range(n):
    if a[i] == 0:
        if left[j] == i + 1:
            left[j], left[l - 1] = left[l - 1], left[j]
        else:
            if j == l - 2:
                if left[l - 1] == rem[j + 1]:
                    left[j], left[l - 1] = left[l - 1], left[j]
        a[i] = left[j]
        j += 1

for i in a:
    print(i, end=' ')
print('')