for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    perform = [0 for i in range(n)]
    rec = [0 for i in range(n)]
    for i in range(n):
        rec[s[i] - 1] = i
    # print(rec)
    op = n - 1
    # lim_for_n = 0
    for i in range(n):
        if op == 0:
            break
        p = rec[i] - 1
        temp = op
        tempP = p
        lim = p + 1

        while tempP >= 0 and temp > 0:
            if perform[tempP] == 1:
                break
            if s[tempP] > i + 1 and perform[p] == 0:
                lim = tempP
            tempP -= 1
            temp -= 1
        # print('for ', i + 1, lim, 'p', p)
        # print('p', p)
        while p >= lim and op > 0:
            rec[i] = p
            s[p], s[p + 1] = s[p + 1], s[p]
            perform[p] = 1
            # print(p + 1)
            # print("s, ", s[p + 1])
            rec[s[p + 1] - 1] = p + 1
            p -= 1
            op -= 1
            # print('inter', s, i + 1)

    for i in s:
        print(i, end=' ')
    print('')
