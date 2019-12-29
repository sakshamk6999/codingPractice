from collections import defaultdict
# ans = defaultdict(int)
mod = 10**9 + 7
ans = [0 for i in range(10**6)]
ans[0] = 1
product = 1
for i in range(1, 10**6):
    product = ((product % mod) * ((i + 1) % mod))%mod
    ans[i] = (((ans[i - 1]%mod) * product) % mod)

for i in range(int(input())):
    number = int(input())
    print(ans[number - 1])
    # print(dp[n - 1])
