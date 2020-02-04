for _ in range(int(input())):
    a, b, c, n = map(int, input().split())
    d = a + b + c - 3 * max(a, b, c)
    d = -1 * d
    if n >= d:
        n -= d
        # print(n)
        if n % 3 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('NO')