for _ in range(int(input())):
    N = input()
    n = list(map(int, list(N)))
    m = len(n)
    p = 0
    while n[0] == 0:
        m -= 1
        p += 1
    t = n[p]
    n = n[p:]
    ans = 9 * (m - 1) + n[0] - 1
    # n.sort()
    if int(str(n[0]) * m) <= int(N):
        ans += 1

    print(ans)