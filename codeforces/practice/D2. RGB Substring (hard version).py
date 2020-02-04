from collections import defaultdict
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = list(input())
    rec = defaultdict(list)
    de = {}
    de['R'] = 1
    de['G'] = 2
    de['B'] = 3
    for i in range(n):
        if (i + 1) % 3 == 1:
            rec[de[s[i]]].append(0)
            for j in {1, 2, 3}:
                if j != de[s[i]]:
                    rec[j].append(1)
        elif (i + 1) % 3 == 2:
            if de[s[i]] == 2:
                t = 1
            elif de[s[i]] == 3:
                t = 2
            else:
                t = 3
            rec[t].append(0)
            for j in {1, 2, 3}:
                if j != t:
                    rec[j].append(1)
        else:
            if de[s[i]] == 3:
                t = 1
            elif de[s[i]] == 2:
                t = 3
            else:
                t = 2
            rec[t].append(0)
            for j in {1, 2, 3}:
                if j != t:
                    rec[j].append(1)

    pref = defaultdict(list)
    pref[1].append(rec[1][0])
    pref[2].append(rec[2][0])
    pref[3].append(rec[3][0])

    for i in range(1, n):
        # print(pref[3])
        # print(rec[3])
        pref[1].append(rec[1][i] + pref[1][i - 1])
        pref[2].append(rec[2][i] + pref[2][i - 1])
        pref[3].append(rec[3][i] + pref[3][i - 1])
        # print(pref[3])
        # print(rec[3])
    # for i in range(1, 4):
    #     print('rec', rec[i])
    #     print('pref', pref[i])
    ans = float('inf')
    # for j in range(1, 4):
    #     ans = min(ans, pref[j][k - 1])
    for i in range(1, n - k):
        for j in range(1, 4):
            ans = min(ans, pref[j][i + k - 1] - pref[j][i - 1])
    print(ans)

