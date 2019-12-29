for _ in range(int(input())):
    a, b, n, s = map(int, input().split())
    x = n * min(a, s//n)
    if b >= s - x:
        print('YES')
    else:
        print('NO')