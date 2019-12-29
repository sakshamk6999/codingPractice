for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    rec = {}
    for i in range(n):
        rec[a[i]] = i
    # print(rec)
    ans = 0
    lim = 0
    for i in range(m):
        if rec[b[i]] > lim:
            ans += 2*(rec[b[i]] - i) + 1
            lim = rec[b[i]]
        else:
            ans += 1

    print(ans)