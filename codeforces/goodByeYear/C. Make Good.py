for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    x = a[0]
    for i in range(1, n):
        x = x ^ a[i]

    if 2*x == s:
        print(0)
        print('')
    else:
        print(2)
        print(x, s + x)