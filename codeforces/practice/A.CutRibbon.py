n, a, b, c = map(int, input().split())

dp = [0 for i in range(n + 1)]
possible = [0 for i in range(n + 1)]
for i in range(n + 1):
    if i >= min(a, b, c):
        dp[i] = max((1 + dp[i - a - 1]) if i - a - 1 >= 0 and possible[i - a - 1] else 0,
                    (1 + dp[i - b - 1]) if i - b - 1 >= 0 and possible[i - b - 1] else 0,
                    (1 + dp[i - c - 1]) if i - c - 1 >= 0 and possible[i - c - 1] else 0)
        if dp[i] != 0:
            possible[i] = 1

print(dp[n])