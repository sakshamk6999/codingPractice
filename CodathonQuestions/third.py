from math import ceil
n, m, l = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0 for i in range(n)] for i in range(m)]
t = 10**9 + 7
for i in a:
    dp[i%m][0] += 1

for i in range(1, n):
    for j in range(m):
        for k in range(m):
            dp[j][i] += (dp[k][i - 1] * dp[(j - k)% m][0]) % t
            dp[j][i] = dp[j][i] % t
# for i in dp:
#     print(i)
print(dp[0][n - 1] % t)