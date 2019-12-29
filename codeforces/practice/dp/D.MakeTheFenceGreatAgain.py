for _ in range(int(input())):
    n = int(input())
    h = [0 for i in range(n)]
    p = [0 for i in range(n)]
    for i in range(n):
        hi, pi = map(int, input().split())
        h[i] = hi
        p[i] = pi

    m = [0 for i in range(n)]
    dp = [0 for i in range(n)]
    for i in range(1, n):
        if h[i] == h[i - 1]:
            if i == 1:
                dp[1] = min(p[0], p[1])
                if min(p[0], p[1]) == p[1]:
                    m[1] = 1
                    h[1] += 1
                else:
                    m[0] = 1
                    h[0] += 1
            else:
                if m[i - 1] == 1:
                    dp[i] = min(dp[i - 2] + p[i - 2], dp[i - 1] + p[i - 1], dp[i - 1] + p[i])
                    if dp[i] == dp[i - 1] + p[i]:
                        m[i] = 1
                        h[i] += 1
                else:
                    dp[i] = min(dp[i - 1] + p[i - 1], dp[i - 1] + p[i])
                    if dp[i] == dp[i - 1] + p[i]:
                        m[i] = 1
                        h[i] += 1
        else:
            dp[i] = dp[i - 1]


    print(dp[n - 1])