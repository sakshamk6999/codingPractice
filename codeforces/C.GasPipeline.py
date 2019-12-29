for _ in range(int(input())):
    n, a, b = map(int, input().split())
    aList = list(map(int, list(input())))
    dp = [[0, 0] for i in range(n + 1)]
    dp[1] = [b, 0]
    for i in range(2, n):
        if aList[i - 1] == 1:
            if dp[i - 1][1] == 0:
                dp[i] = [dp[i - 1][0] + 2*a + 2 * b, 1]
            else:
                dp[i] = [dp[i - 1][0] + a + 2 * b, 1]
        else:
            if dp[i - 1][1] == 0:
                dp[i] = [dp[i - 1][0] + a + b, 0]
            else:
                if min(dp[i - 1][0] + a + 2 * b, dp[i - 1][0] + 2 * a + b) == dp[i - 1][0] + a + 2 * b:
                    dp[i] = [dp[i - 1][0] + a + 2 * b, 1]
                else:
                    dp[i] = [dp[i - 1][0] + 2 * a + b, 0]
    print(dp)
    if dp[n - 1][1] == 1:
        print(dp[n - 1][0] + b + 2 * a)
    else:
        print(dp[n - 1][0] + b + a)
