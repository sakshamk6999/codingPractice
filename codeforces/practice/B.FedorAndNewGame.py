n, m, k = map(int, input().split())
p = []

for _ in range(m):
    p.append(int(input()))

c = int(input())

r = 0

for i in p:
    xor = i ^ c
    count = 0
    while xor:
        xor = xor & (xor - 1)
        count += 1

    if count <= k:
        r += 1
print(r) 