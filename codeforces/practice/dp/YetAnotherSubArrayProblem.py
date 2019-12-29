from math import  ceil
n, m, k = map(int, input().split())
a = list(map(int, input().split()))
dp = [[0, 0, 0]for i in range(n + 1)]

for i in range(1, n + 1):
    tempAns = dp[i - 1][0] + a[i - 1] - k * ceil((dp[i - 1][1] + 1)/m)
    if max(tempAns, a[i - 1] - k) == a[i - 1] - k:
        dp[i] = [a[i - 1], 1, a[i - 1] - k]
    else:
        dp[i] = [dp[i - 1][0] + a[i - 1], dp[i - 1][1] + 1, tempAns]

#
# ans = dp[n][0] - k * ceil(dp[n][1]/m)
print(max(dp[n][2], 0))

