from collections import defaultdict
for _ in range(int(input())):
    s = list(input())
    rec = {}
    rec = defaultdict(lambda : -1, )
    ans = []
    i = 0
    n = len(s)
    while i < n:
        j = i
        temp = 0
        while j < n and s[j] == s[i]:
            temp += 1
            j += 1
        if temp % 2 == 0 and rec.get(s[i], 0) != 1:
            rec[s[i]] = -1
        else:
            if rec.get(s[i], 0) != 1:
                ans.append(s[i])
                rec[s[i]] = 1
            # elif rec.get()
        i = j

    ans.sort()
    for i in ans:
        print(i, end='')
    print('')