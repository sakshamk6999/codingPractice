n = int(input())
a = list(map(int, input().split()))
neg = []
l = 0

for i in range(n):
    if a[i] < 0:
        neg.append(i)
        l += 1
numPos = 0
