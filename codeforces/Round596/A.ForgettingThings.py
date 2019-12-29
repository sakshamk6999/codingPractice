a, b = map(int, input().split())
if a == b:
    print(str(a) + '0', str(a) + '1')

elif a > b:
    if a == 9 and b == 1:
        print(9, 10)
    else:
        print(-1)
else:
    if b - a == 1:
        print(str(a) + '9', str(b) + '0')
    else:
        print(-1)