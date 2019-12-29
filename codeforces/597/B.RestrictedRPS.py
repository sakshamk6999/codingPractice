import math
for _ in range(int(input())):
    n = int(input())
    r, p, s = map(int, input().split())
    a = list(input())
    br, bp, bs = 0, 0, 0
    for i in a:
        if i == 'R':
            br += 1
        elif i == 'P':
            bp += 1
        else:
            bs += 1

    win = math.ceil(n//2)
    winr = min(r, bs)
    winp = min(p, br)
    wins = min(s, bp)
    temp = min(r, bs) + min(p, br) + min(s, bp)
    if temp < win:
        print('NO')
    else:
        print('YES')
        for i in a:
            if i == 'R':
                br -= 1
                if p > 0:
                    p -= 1
                    print('P', end='')
                    winp -= 1
                else:
                    if r > winr:
                        print('R')
                        r -= 1
                    else:
                        print('S')
                        s -= 1
            elif i == 'P':
                bp -= 1
                if s > 0:
                    s -= 1
                    print('S', end='')
                    wins -= 1
                else:
                    if r > winr:
                        print('R')
                        r -= 1
                    else:
                        print('P')
                        p -= 1
            else:
                bs -= 1
                if r > 0:
                    r -= 1
                    print('R', end='')
                    winr -= 1
                else:
                    if s > wins:
                        print('S')
                        s -= 1
                    else:
                        print('P')
                        p -= 1
        print('')