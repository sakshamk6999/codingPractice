import math
from collections import defaultdict
def primeFactors(n, record):
    ans = []
    while n % 2 == 0:
        if record[2] == 0:
            record[2] = 1
            ans.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            if record[i] == 0:
                ans.append(int(i))
                record[i] = 1
            n = n / i
    if n > 2:
        ans.append(n)
    return ans
n = int(input())
record = {}
record = defaultdict(lambda : 0, record)

ans = primeFactors(n, record)
if len(ans) == 1:
    print(ans[0])
else:
    print(1)