for _ in range(int(input())):
    n, s = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    ai = -1
    m = -1
    flag = 0
    for i in range(n):
        if flag == 0:
            if s >= a[i]:
                s -= a[i]
                ans += 1
                m = max(a[i], m)
                if m == a[i]:
                    ai = i
            else:
                initialAns = ans
                ans -= 1
                flag = 1
                s += m
                if s >= a[i]:
                    s -= a[i]
                    ans += 1
                else:
                    break
        else:
            if s >= a[i]:
                s -= a[i]
                ans += 1
            else:
                break
    if flag == 0:
        print(0)
    else:
        if ans >= initialAns:
            print(ai + 1)
        else:
            print(0)
