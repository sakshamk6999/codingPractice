a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
#for minimum
temp = n
temp = max(0, temp - (a1*(k1 - 1)) - (a2*(k2 - 1)))
minAns = temp
#for maximum
if k1 < k2:
    remove = min(a1, n//k1)
    n = n - remove*k1
    if n > 0:
        remove += min(a2, n//k2)

elif k2 <= k1:
    remove = min(a2, n//k2)
    n = n - remove*k2
    if n > 0:
        remove += min(a1, n//k1)

print(minAns, remove)