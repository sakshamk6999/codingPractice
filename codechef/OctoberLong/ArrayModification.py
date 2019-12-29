for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    f = k//n
    if n %2 != 0 and f:
        a[n//2] = 0
    f = f % 3
    fr = k % n
    for i in range(f):
        for j in range(n):
            a[j] = a[j] ^ a[n - j - 1]

    for i in range(fr):
        a[i] = a[i] ^ a[n - i - 1]

    for i in range(n):
        print(a[i], end=' ')

    print('')