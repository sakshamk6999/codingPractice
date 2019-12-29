t = 10 ** 9 + 7
N = 10 ** 5

fac = [1 for i in range(N + 1)]
for i in range(2, N + 1):
    fac[i] = ((fac[i - 1] % t)*(i % t)) % t

def ncr(n, r):
    return (fac[n] * pow(fac[r], t - 2, t) * pow(fac[n - r], t - 2, t)) % t

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, list(input())))
    b = list(map(int, list(input())))
    aOne = sum(a)
    bOne = sum(b)
    l = abs(aOne - bOne)
    r = aOne + bOne
    if r > n:
        while r > n:
            r -= 2
    ans = 0
    for i in range(l, r + 1, 2):
        ans += ncr(n, i)

    print(ans % t)