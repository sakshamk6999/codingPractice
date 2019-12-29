for _ in range(int(input())):
    a, m = map(int, input().split())
    ans = 0
    l = []
    x = 1
    t = a
    while a <= m:
        a = t*x
        # print(a)
        if m % (a + 1) == 0:
            ans += 1
            l.append((m*x)//(a + 1))
        x += 1

    print(ans)
    for i in l:
        print(i, end=' ')
    print('')