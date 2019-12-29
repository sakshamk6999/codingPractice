for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, list(input())))
    i = 0
    temp = 0
    prev = 0
    while i < n and k > 0:
        if a[i] == 1:
            i += 1
            # temp += 1
        else:
            sw = min(k, i - prev)
            k -= sw
            a[i - sw], a[i] = a[i], a[i - sw]
            prev = i - sw + 1
            i += 1

    for i in a:
        print(i, end='')
    print('')