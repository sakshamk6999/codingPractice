def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

n = int(input())
a = sorted(list(map(int, input().split())))


if n == 2:
    print(1, a[1] - a[0])
else:
    t = a[n - 1] - a[0]
    for i in range(1, n):
        t = gcd(t, a[n - 1] - a[i])

    ans = 0
    for i in range(n - 1):
        ans += (a[n - 1] - a[i])//t

    print(ans, t)