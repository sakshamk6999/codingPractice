for _ in range(int(input())):
    n = int(input())
    ans = 1
    flag = 0
    a = list(map(int, input().split()))
    for i in range(1, n):
        j = i - 1
        flag = 0
        while j >= 0 and j >= i - 5:
            if a[j] > a[i]:
                j -= 1
            else:
                flag = 1
                break
        if flag == 0:
            ans += 1

    print(ans)