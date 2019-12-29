for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = m * (n // m)
    n -= ans

    ans += min(m//2, n)
    print(ans)