n = int(input())
a = list(map(int, input().split()))
dp = [1 for i in range(n)]
for i in range(n - 2, -1, -1):
    if a[i + 1] <= 2 * a[i]:
        dp[i] = dp[i + 1] + 1

print(max(dp))
