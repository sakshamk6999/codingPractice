for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    flag = 0
    for i in range(n - 1):
        if abs(a[i] - a[i + 1]) >= 2:
            flag = 1
            t = i + 1
            break

    if flag == 1:
        print('YES')
        print(t, t + 1)
    else:
        print('NO')
