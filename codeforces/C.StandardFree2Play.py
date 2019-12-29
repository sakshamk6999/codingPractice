    from collections import defaultdict
    for _ in range(int(input())):
        h, n = map(int, input().split())
        mov = list(map(int, input().split()))
        # rec = {}
        # rec = defaultdict(int)
        # for i in mov:
        #     rec[i] = 1

        i = h
        ans = 0
        # while i > 0:
        #     if i <= 2:
        #         break
        #     if rec.get(i - 1, 0) == 0:
        #         i -= 1
        #     else:
        #         if rec.get(i - 2, 0) == 0:
        #             ans += 1
        #         i -= 2
        # curr = h
        # next = 1
        # while next < n:
        #     if mov[next] == h - 2:
        #         h -= 2
        #         next += 1
        #     else:
        #
        dp = [0 for i in range(n)]
        # if mov[n - 1] % 2 == 0:
        #     dp[n - 1] = (mov[n - 1] - 1) // 2
        # else:
        #     dp[n - 1] = (mov[n - 1] - 2) // 2
        for i in range(n - 2, -1, -1):
            if mov[i] <= 2 or mov[i + 1] <= 1:
                dp[i] = 0
            elif i + 2 < n and mov[i + 1] - mov[i + 2] == 1:
                dp[i] = min(dp[i + 2], 1 + dp[i + 1])
            else:
                dp[i] = 1 + dp[i + 1]
        print(dp[0])