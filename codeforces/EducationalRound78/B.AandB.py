for _ in range(int(input())):
    a, b = map(int, input().split())
    if a == b:
        print(0)
    else:
        i = 1
        while 1:
            r = (i * (i + 1))//2
            if (abs(b - a) + r) % 2 == 0 and (abs(b - a) + r) // 2 <= r:
                break
            i += 1
        print(i)