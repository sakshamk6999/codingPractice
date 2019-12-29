for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        rem = n - i
        for j in range(a[i], -1, -1):
            if rem >= j:
                ans = max(ans, j)
                break

    print(ans)