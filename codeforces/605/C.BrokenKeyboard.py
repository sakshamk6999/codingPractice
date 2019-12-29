from collections import defaultdict
n, k = map(int, input().split())
s = list(input())
rec = {}
rec = defaultdict(lambda : 0, rec)
avail = input().split()
for i in avail:
    rec[i] = 1

t = 0
ans = 0
for i in s:
    if rec[i] == 1:
        t += 1
    else:
        ans += (t*(t + 1))//2
        t = 0
ans += (t*(t + 1))//2
print(ans)