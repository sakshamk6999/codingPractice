for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    while n >= 3:
        t = sorted([a[0], a[1], a[2]])
        a.remove(t[1])
        n -= 1

    for i in a:
        print(i, end= ' ')

    print('')