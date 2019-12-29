for _ in range(int(input())):
    a, b, c, r = map(int, input().split())
    if b < a:
        b, a = a, b
    mi = c - r
    ma = c + r
    if mi <= b and ma >= a:
        if mi < a:
            mi = a
        if ma > b:
            ma = b
        print(b - a - (ma - mi))
    else:
        print(b - a)