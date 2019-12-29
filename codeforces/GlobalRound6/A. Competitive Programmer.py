for _ in range(int(input())):
    a = sorted(list(map(int, list(input()))))
    e = 0
    z = 0
    for i in a:
        if i % 2 == 0 and i != 0:
            e = 1
            break
        elif i == 0:
            z += 1
    if z >= 2:
        e = 1
    if a[0] == 0 and sum(a) % 3 == 0 and e == 1:
        print('red')
    else:
        print('cyan')