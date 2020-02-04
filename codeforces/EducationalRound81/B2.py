from collections import defaultdict
for _ in range(int(input())):
    n, x = map(int, input().split())
    s = list(map(int, list(input())))
    rec = defaultdict(int)
    pre = [0 for i in range(n)]
    pre[0] = 1 if s[0] == 1 else -1
    rec[pre[0]] = 1
    for i in range(1, n):
        pre[i] = pre[i - 1] + 1 if s[i] == 1 else pre[i - 1] - 1
        # print(pre[i])
        rec[pre[i]] = 1 if rec.get(pre[i], 0) == 0 else rec[pre[i]] + 1

    a = n - 2 *pre[n - 1]
    ans = 0
    print(rec.keys())
    for i in rec.keys():
        if a != 0 and (x - i) % a == 0:
            ans += rec[pre[i]]
    print(ans)