for _ in range(int(input())):
    n = int(input())
    s1 = list(input())
    s2 = list(input())
    d = 0
    temp = []
    flag = 1
    for i in range(n):
        if s1[i] != s2[i]:
            if d == 0:
                temp = [s1[i], s2[i]]
                flag = 0
            else:
                if d > 1:
                    flag = 0
                    break
                else:
                    if temp != [s1[i], s2[i]]:
                        flag = 0
                        break
                    else:
                        flag = 1
            d += 1

    if flag == 1:
        print('Yes')
    else:
        print('No')

