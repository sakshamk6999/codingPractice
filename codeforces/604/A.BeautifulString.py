from collections import defaultdict
for _ in range(int(input())):
    s = list(input())
    l = ['a', 'b', 'c']
    n = len(s)
    rec = defaultdict(int)
    flag = 1
    for i in l:
        rec[i] = 0
    for i in range(n):
        if s[i] == '?':
            if i == n - 1:
                for j in l:
                    if rec[j] == 0:
                        s[i] = j
                break

            if s[i + 1] == '?':
                for j in l:
                    if rec[j] == 0:
                        s[i] = j
            else:
                rec[s[i + 1]] += 1
                for j in l:
                    if rec[j] == 0:
                        s[i] = j
                rec[s[i + 1]] -= 1

        else:
            if i < n - 1 and s[i] == s[i + 1]:
                flag = 0
                break

        if i > 0:
            rec[s[i - 1]] -= 1
        rec[s[i]] += 1

    if flag:
        print(''.join(s))
    else:
        print(-1)
