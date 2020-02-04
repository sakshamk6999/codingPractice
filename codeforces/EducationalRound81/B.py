for _ in range(int(input())):
    n, x = map(int, input().split())
    s = list(map(int, list(input())))
    flag = 0
    pre = [0 for i in range(n)]
    if x < 0:
        flag = 1
        for i in range(n):
            s[i] = 1 if s[i] == 0 else 0
            pre[i] = pre[i - 1] + s[i] if i > 0 else s[i]
    temp = n - 2*sum(s)
    # print(temp)
    if temp < 0:
        print(0)
    else:
        isInf = 0
        ans = 0
        tempX = x - (temp*(x//temp)) if temp != 0 else 0
        tempX = x - tempX
        # r = -1
        for i in range(n):
            # print('tempX', tempX)

            if tempX == x:
                if temp == 0:
                    isInf = 1
                    break
                ans += 1
            if flag == 0:
                if s[i] == 0:
                    tempX -= 1
                else:
                    tempX += 1
            else:
                if s[i] == 0:
                    tempX += 1
                else:
                    tempX -= 1

        tempX = x - (temp * (x // temp)) if temp != 0 else 0
        tempX = x - tempX
        for i in range(n - 1, -1, -1):
            if flag == 1:
                if s[i] == 0:
                    tempX -= 1
                else:
                    tempX += 1
                if tempX == x:
                    if temp == 0:
                        isInf = 1
                        break
                    ans += 1
            else:
                if s[i] == 0:
                    tempX += 1
                else:
                    tempX -= 1
                if tempX == x:
                    if temp == 0:
                        isInf = 1
                        break
                    ans += 1

        if isInf == 1:
            print(-1)
        else:
            print(ans)