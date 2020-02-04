for _ in range(int(input())):
    n = int(input())
    s = list(map(int, list(input())))
    no = 0
    a = []
    for i in range(n):
        if s[i] % 2 != 0:
            no += 1
            a.append(s[i])
        if no == 2:
            break
    if no == 2:
        print(str(a[0]) + str(a[1]))
    else:
        print(-1)