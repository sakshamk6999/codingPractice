for _ in range(int(input())):
    n, m, q = map(int, input().split())
    e = 0
    o = 0
    ans  = 0
    r = [0 for i in range(n)]
    c = [0 for i in range(m)]
    for i in range(q):
        x, y =map(int, input().split())
        r[x - 1]+= 1
        c[y - 1]+= 1
    for i in range(n):
        if r[i] % 2 == 0:
            e += 1
        else:
            o += 1

    for i in range(m):
        if c[i] % 2 == 0:
            ans += o
        else:
            ans += e

    print(ans)