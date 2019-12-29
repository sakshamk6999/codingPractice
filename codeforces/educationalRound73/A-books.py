for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = [0 for i in range(n)]
    for i in range(n - 2, -1, -1):
        if a[i] == a[i + 1]:
            dp[i] = dp[i + 1]
        else:
            dp[i] = n - 1 - i
    for i in dp:
        print(i, end=" ")
    print('')