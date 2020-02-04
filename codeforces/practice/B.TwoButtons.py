n, m = map(int, input().split())
ans = 0
if n >= m:
    ans = n - m
else:
    while m > n:
        if m % 2 == 0:
            if m // 2 <= n:
                ans += 1 + n - m//2
                break
            m = m // 2
        else:
            m += 1
        ans += 1
    # ans += m - n
print(ans)