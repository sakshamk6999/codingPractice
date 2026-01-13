from collections import defaultdict

MOD = 10**9 + 7

n, l, m = map(int, input().split())
a = map(int, input().split())
b = map(int, input().split())
c = map(int, input().split())

dp = [[0 for i in range(m)] for i in range(l)]

initial_rem = defaultdict(int)
layer_rem = defaultdict(int)
final_rem = defaultdict(int)

for i in a:
    initial_rem[i%m] += 1

for i in b:
    layer_rem[i%m] += 1

for i in c:
    final_rem[i%m] += 1

for i in range(l):
    for r in range(m):
        if i == 0:
            dp[i][r] = initial_rem[r]
        else:
            dp[i][r] = (dp[i - 1][r if r == 0 else m - r] * layer_rem[r]) % MOD

ans = 0

for r in range(m):
    ans += (dp[l - 1][r if r == 0 else m - r] * final_rem[r]) % MOD

print(ans % MOD)