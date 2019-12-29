a, b, c, d = map(int, input().split())
s = sum([a, b, c, d])
# print(s)
if s % 2 != 0:
    print('NO')
else:
    s = s//2
    # print(s)
    if a == s or b == s or c == s or d == s:
        print('YES')
    elif a+b == s or a+c == s or a+d == s or b+c == s or b+d == s or c+d == s:
        print('YES')
    else:
        print('NO')