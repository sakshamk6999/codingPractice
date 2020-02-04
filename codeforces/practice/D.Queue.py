n = int(input())
a = sorted(list(map(int, input().split())))

diss = 0
wait = 0
for i in range(n):
    if wait <= a[i]:
        wait += a[i]
    else:
        diss += 1

print(n - diss)