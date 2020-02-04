m = 10**9 + 7
t, k = map(int, input().split())
dp = [0 for i in range(10**5 + 1)]
dp[0] = 1
s = [0 for i in range(10**5 + 1)]
s[0] = 1

for i in range(1, 10**5 + 1):
    # print(i - 1, dp[i - 1])
    if i < k:
        dp[i] = 1
    else:
        dp[i] = (dp[i - 1] + dp[i - k])%m
    s[i] = (s[i - 1] + dp[i]) % m

# print(dp)
for i in range(t):
    l, r = map(int, input().split())
    print((s[r] + m - s[l - 1])%m)
