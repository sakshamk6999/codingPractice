for _ in range(int(input())):
    s = list(input())
    ans = []
    n = len(s)
    a = 0
    if len(s) < 3:
        print(0)
        print('')
    else:
        i = 0
        while i < n - 2:
            if s[i] + s[i + 1] + s[i + 2] == 'one':
                ans.append(i + 1)
                a += 1
                i += 3
            elif s[i] + s[i + 1] + s[i + 2] == 'two':
                if i + 4 < n and s[i + 3] + s[i + 4] == 'ne':
                    ans.append(i + 2)
                    a += 1
                    i += 5
                else:
                    ans.append(i + 1)
                    i += 3
                    a += 1
            else:
                i += 1
        print(a)
        for i in ans:
            print(i + 1, end=' ')
        print('')