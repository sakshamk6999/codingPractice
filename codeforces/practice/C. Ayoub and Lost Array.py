from math import ceil
n, l, r = map(int, input().split())
dp_0 = [0 for i in range(n)]
dp_1 = [0 for i in range(n)]
dp_2 = [0 for i in range(n)]
t = 10**9 + 7
dp_0[0] = (r//3 - ceil(l/3) + 1)
dp_1[0] = ((r - 1)//3 - ceil((l - 1)/3) + 1)
dp_2[0] = ((r - 2)//3 - ceil((l - 2)/3) + 1)

for i in range(1, n):
    dp_0[i] = ((dp_0[i - 1] * dp_0[0])%t + (dp_1[i - 1] * dp_2[0])%t + (dp_2[i - 1] * dp_1[0])%t)%t
    dp_1[i] = ((dp_0[i - 1] * dp_1[0])%t + (dp_1[i - 1] * dp_0[0])%t + (dp_2[i - 1] * dp_2[0])%t)%t
    dp_2[i] = ((dp_0[i - 1] * dp_2[0])%t + (dp_1[i - 1] * dp_1[0])%t + (dp_2[i - 1] * dp_0[0])%t)%t

# print(dp_0)
# print(dp_1)
# print(dp_2)
print(dp_0[n - 1]%t)