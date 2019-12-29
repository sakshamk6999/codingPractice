s = list(input())
n = len(s)
dp = ['Mike' for i in range(n)]
start = 0
print(dp[0])
for i in range(1, n):
    if s[i] > s[start]:
        dp[i] = 'Mike' if s[start] == 'Ann' else 'Ann'

    else:
        dp[i] = 'Mike'
        start = i
    print(dp[i])