import math
def primeFactors(n, primeFactors):
    while n % 2 == 0:
        primeFactors.add(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            primeFactors.add(int(i))
            n = n / i

    if n > 2:
        primeFactors.add(n)

x, n = map(int, input().split())
mod = 10**9 + 7
primes = set()
primeFactors(x, primes)
# rec = {}
ans = 1
for i in primes:
    temp = i
    p = 1
    while temp <= n:
        p += 1
        temp = temp * i
    p -= 1
    print(i, p)
    if p > 1:
        ans *= (max(((pow(i, p*2) - 1)//(i + 1)) % mod, 1) * (((i**p) % mod)*((n - (i**p) + 1) % mod) % mod)) % mod
    ans = ans % mod

print(ans)