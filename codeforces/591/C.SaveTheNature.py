for _ in range(int(input())):
    n = int(input())
    p = sorted(list(map(int, input().split())))
    x, a = map(int, input().split())
    y, b = map(int, input().split())
    t = int(input())
    pos = []
    l = 0
    for i in range(1, n + 1):
        if i % a == 0 and i % b != 0:
            pos.append([i, x])
            l += 1
        elif i % b == 0 and i % a != 0:
            pos.append([i, y])
            l += 1
        elif i % a == 0 and i % b == 0:
            pos.append([i, x + y])
            l += 1

    i = 0
    ans = -1
    # while s < t and i < l:
    #     s += pos[i][1] * (p.pop()//100)
    #     print(s)
    #     if s >= t:
    #         ans = pos[i][0]
    #         break
    #     i += 1
    for i in range(l):
        s = 0
        k = n - 1 - i
        for j in sorted(pos[:i + 1], key=lambda temp : temp[1]):
            s += (p[k]//100) * j[1]
            k += 1
        if s >= t:
            ans = pos[i][0]
            break
    print(ans)
