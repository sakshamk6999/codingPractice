n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [0 for i in range(n)]
for i in range(q):

    l, r = map(int, input().split())
    b[l - 1] += 1
    if r < n:
        b[r] -= 1
    # print(b)
for i in range(1, n):
    b[i] += b[i - 1]

b.sort()
a.sort()
ans = 0
# print(b)
for i in range(n):
    ans += a[i] * b[i]

print(ans)