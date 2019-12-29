from collections import defaultdict
for _ in range(int(input())):
    n, m = map(int, input().split())
    x = sorted(list(set(map(int, input().split()))))
    # print(x)
    p = 0
    i = 0
    j = len(x) - 1
    while i < j and i < len(x) and j >= 0:
        p += 1
        while i < j and x[i] - p*m <= 0:
            # print(x[i] - p*m)
            i += 1
            # print(i)
        if i > j:
            # print('YEs')
            break
        j -= 1

        # print(i, j, p)
    if i == j:
        p += 1
    print(p)