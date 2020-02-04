t = 10**9 + 7
n, m = map(int, input().split())

dp =[[[0 for i in range(n + 1)]for i in range(n + 1)]for i in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        dp[i][j][j] = ((n - j + 1)*(n - j + 2))//2
        for k in range(1, n + 1):
            dp[i][j][k] = ((dp[i - 1][j][k]) * ((k - j) * (k + 1) + ((k + 1)*(k + 2))//2)) % t

for i in dp[n]:
    print(i)
