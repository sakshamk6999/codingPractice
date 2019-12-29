a, b, c, d = map(int, input().split())
flag = 1

if b < a:
    if c != 0 or d != 0:
        flag = 0
    else:
        if b + 1 < a:
            flag = 0
        else:
            ans = "0 " + "1 0 " * b

    if flag == 0:
        print('NO')
    else:
        print('YES')
        print(ans)

elif c < d:
    if a != 0 or b != 0:
        flag = 0
    else:
        if c + 1 < d:
            flag = 0
        else:
            ans = "3 " + "2 3 " * c

    if flag == 0:
        print('NO')
    else:
        print('YES')
        print(ans)

else:
    zone = "0 1 " * a
    b -= a
    thwo = "2 3 " * d
    c -= d
    if abs(b - c) > 1:
        flag = 0
    else:
        mid = "2 1 " * min(b, c)
        if b > c:
            ans = "1" + " " + zone + mid + thwo
        else:
            ans = zone + mid + thwo + "2"

    if flag == 0:
        print('NO')
    else:
        print('YES')
        print(ans)
