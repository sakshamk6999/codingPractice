for _ in range(int(input())):
    n, m, k = map(int, input().split())
    h = list(map(int, input().split()))
    block = m
    flag = 1
    for i in range(n - 1):
        block += h[i] - max(0, h[i + 1] - k)
        if block < 0:
            flag = 0
            break
    if flag == 0:
        print('NO')
    else:
        print('YES')
