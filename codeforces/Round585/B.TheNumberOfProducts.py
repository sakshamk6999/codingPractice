n = int(input())
a = list(map(int, input().split()))
neg = []
l = 0
for i in range(n):
    if a[i] < 0:
        neg.append(i)
        l += 1

ans = 0
if l != 0:
    dp = [[0, 0] for i in range(l)]
    dp[0][0] = (neg[0] * (neg[0] + 1))//2
    dp[0][1] = neg[0] + 1
    print(dp[0])
    for i in range(1, l):
        if i % 2 != 0:
            rem = neg[i] - neg[i - 1] - 1
            dp[i][0] = dp[i - 1][0] + 1 + ((rem * (rem + 1))//2)
            dp[i][1] = dp[i - 1][1] + rem + 1
        else:
            rem = neg[i] - neg[i - 1] - 1
            dp[i][0] = dp[i - 1][0] + ((rem * (rem + 1)) // 2)
            dp[i][1] = dp[i - 1][1] + rem + 2
        print(dp[i])
    rem = (n - 1 - neg[l - 1])
    print(dp[l - 1][1] + rem, dp[l - 1][0] + (rem*(rem + 1))//2)
else:
    print((n*(n + 1))//2)