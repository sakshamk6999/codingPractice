from collections import defaultdict
q, x = map(int, input().split())
rem = defaultdict(int)
num = defaultdict(int)
turn = [0 for i in range(q)]
a = 0
for i in range(q):
    t = int(input())
    turn[i] = t
    rem[t % x] = 1 if rem.get(t % x, 0) == 0 else rem[t % x] + 1
    num[t] = 1 if num.get(t, 0) == 0 else num[t] + 1
    l = 0
    r = 0
    # calculation of l
