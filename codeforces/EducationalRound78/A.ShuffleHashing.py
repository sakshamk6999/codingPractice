from collections import defaultdict
for _ in range(int(input())):
    a = list(input())
    b = list(input())
    rec_a = {}
    rec_a = defaultdict(lambda: 0, rec_a)
    rec_b = {}
    rec_b = defaultdict(lambda: 0, rec_b)
    if len(a) <= len(b):
        for i in a:
            rec_a[i] += 1

        for i in range(len(a) - 1):
            # print(i)
            # print(b[i])
            rec_b[b[i]] += 1
        i = len(a) - 1
        flag = 0
        sa = set(a)
        while i < len(b):
            # print(b[i], end=' ')

            rec_b[b[i]] += 1
            for j in sa:
                if rec_b[j] != rec_a[j]:
                    flag = 0
                    break
                else:
                    flag = 1
            if flag == 0:
                i += 1
                rec_b[b[i - len(a)]] -= 1
            else:
                break
            # print('')

        if flag == 0:
            print('NO')
        else:
            print('YES')
    else:
        print('NO')