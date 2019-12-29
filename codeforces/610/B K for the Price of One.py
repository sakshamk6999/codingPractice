for _ in range(int(input())):
    n, p, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    leftMoney = [0 for i in range(n)]
    dp = [0 for i in range(n)]
    leftMoney[0] = p
    for i in range(n):
        if i >= k - 1:
            if leftMoney[i] >= a[i]:
                dp[i] = dp[i - 1] + 1
                if i + 1 < n:
                    leftMoney[i + 1] = leftMoney[i] - a[i]
            else:
                dp[i] = dp[i - 1]
                if i + 1 < n:
                    leftMoney[i + 1] = leftMoney[i]

            if leftMoney[i - k + 1] >= a[i]:
                dp[i] = max(dp[i], k + (dp[i - k] if i >= k else 0))
                if i + 1 < n:
                    leftMoney[i + 1] = leftMoney[i - k + 1] - a[i]
        else:
            if leftMoney[i] >= a[i]:
                dp[i] = dp[i - 1] + 1
                if i + 1 < n:
                    leftMoney[i + 1] = leftMoney[i] - a[i]
            else:
                dp[i] = dp[i - 1]
                if i + 1 < n:
                    leftMoney[i + 1] = leftMoney[i]

    print(dp[n - 1])
