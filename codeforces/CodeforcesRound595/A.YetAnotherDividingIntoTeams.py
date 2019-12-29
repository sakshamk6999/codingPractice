for _ in range(int(input())):
    n = int(input())
    ans = 1
    a = sorted(list(map(int, input().split())))
    for i in range(1, n):
        if a[i] - a[i - 1] == 1:
            ans = 2
            break
    print(ans)
