n = int(input())
a = list(map(int, input().split()))
dp = [[float('inf') for i in range(3)]for i in range(n + 1)]
dp[0][0] = 0
dp[0][1] = 0
dp[0][2] = 0
for i in range(1, n + 1):
    if a[i - 1] == 1 or a[i - 1] == 3:
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])
    if a[i - 1] == 2 or a[i - 1] == 3:
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])
    dp[i][0] = min(dp[i - 1]) + 1

print(min(dp[n]))
