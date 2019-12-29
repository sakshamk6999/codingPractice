for _ in range(int(input())):
    n, k, p = map(int, input().split())
    a = list(map(int, input().split()))
    t = sorted(a)
    if k % 2 != 0:
        if p == 0:
            print(t[n - 1])
        else:
            print(t[0])
    else:
        if p == 0:
            ans = 0
            for i in range(n):
                if i == 0:
                    ans = max(ans, a[i + 1])
                elif i == n - 1:
                    ans = max(ans, a[i - 1])
                else:
                    ans = max(ans, min(a[i - 1], a[i + 1]))
            print(ans)
        else:
            ans = float('inf')
            for i in range(n):
                if i == 0:
                    ans = min(ans, a[i + 1])
                elif i == n - 1:
                    ans = min(ans, a[i - 1])
                else:
                    ans = min(ans, max(a[i - 1], a[i + 1]))
            print(ans)