s = list(input())
n = len(s)
dp = {}
p = {}
for i in range(n):
    p[i, i] = 1
    dp[i, i] = 1
for d in range(1, n):
    for i in range(n - d):
        if d % 2 == 0:
            if s[i] == s[i + d] and p[i + 1, i + d - 1] == 1:
                dp[i, i + d] = dp[i + 1, i + d - 1] + 2
                p[i, i + d] = 1
            else:
                p[i, i + d] = 0
                dp[i, i + d] = max(dp[i + 1, i + d], dp[i, i + d - 1])
        else:
            dp[i, i + d] = max(dp[i + 1, i + d], dp[i, i + d - 1])
ans = 0
for i in range(1, n):
    ans = max(ans, dp[0, i - 1] * dp[i, n - 1])

print(ans)