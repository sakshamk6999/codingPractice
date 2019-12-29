import math
# print(countSetBits(10**9))
n, p = map(int, input().split())
if p == 0:
    print(bin(n).count('1'))
else:
    ans = 0
    while n > 0:
        n -= p
        if n > 0:
            i = int(math.log(n, 2))
            n -= 2**i
            ans += 1
        else:
            n = -1
            break
    if n < 0:
        print(-1)
    else:
        print(ans)