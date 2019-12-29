for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    pos = [0 for i in range(n)]
    for i in range(n):
        pos[p[i] - 1] = i

    ans = ['0' for i in range(n)]
    mi = float('inf')
    ma = 0
    for i in range(n):
        ma = max(ma, pos[i])
        mi = min(mi, pos[i])
        if ma - mi == i:
            ans[i] = '1'

    print(''.join(ans))