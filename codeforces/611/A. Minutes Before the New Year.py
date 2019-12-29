for _ in range(int(input())):
    h, m = map(int, input().split())
    diff = 0
    if h != 0:
        diff = (24 - h) * 60 - m
    else:
        if m == 0:
            diff = 0
        else:
            diff = 24 * 60 - m


    print(diff)