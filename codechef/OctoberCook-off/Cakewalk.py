import math
for _ in range(int(input())):
    n = int(input())
    x, y = 0, 0
    s = 0
    while n % 10 == 0:
        s += 1
        n = n //10
    # print(n)
    y = math.log(n, 2)

    if int(y) == y:
        x = s - int(y)
        if x >= 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')