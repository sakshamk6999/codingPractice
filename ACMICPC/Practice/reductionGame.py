for _ in range(int(input())):
    n, k = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    d = []
    d2 = []
    ld = 0
    for i in a:
        if i > k:
            d.append(i - k)
            d2.append(i - k)
            ld += 1

    i = 0
    ans = sum(a)
    ans2 = ans
    while i < ld - 1:
        ans -= d[i] * 2
        d[i + 1] -= d[i]
        i += 1

    i = 0
    # print("ld", ld)
    j = ld - 1
    # print("ans2, i, j", ans2, i, j)
    while i < j:
        temp = min(d2[i], d2[j])
        d2[i] -= temp
        d2[j] -= temp
        if d2[i] == 0:
            i += 1
        if d2[j] == 0:
            j -= 1
        ans2 -= 2 * temp
        # print("ans2", ans2)

    print(max(ans, ans2))
