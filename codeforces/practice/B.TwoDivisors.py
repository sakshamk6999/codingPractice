def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

for _ in range(int(input())):
    m, n = map(int, input().split())

    g = gcd(max(m, n), min(m, n))

    lcm = (m * n) // g

    if lcm == max(m, n):
        print(max(m,n) * (max(m,n)//min(m,n)))
    else:
        print(lcm)
