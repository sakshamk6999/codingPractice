def fill(i, a, rec):
    p = 1
    j = a[i] - 1
    temp = [i]
    while j != i:
        p += 1
        temp.append(j)
        j = a[j] - 1
    for i in temp:
        rec[i] = p

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = [-1 for i in range(n)]
    for i in range(n):
        if ans[i] == -1:
            fill(i, a, ans)

    for i in ans:
        print(i, end=' ')
    print('')