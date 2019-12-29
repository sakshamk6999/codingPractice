for _ in range(int(input())):
    n = int(input())
    numOdd = 0
    numEvenMisfit = 0
    flag = 0
    for i in range(n):
        s = list(map(int, list(input())))
        if len(s) % 2 != 0:
            flag = 1
            numOdd += 1
        else:
            if sum(s) % 2 != 0:
                numEvenMisfit += 1

    if flag == 1:
        print(n)
    else:
        if numEvenMisfit % 2 != 0:
            print(n - 1)
        else:
            print(n)