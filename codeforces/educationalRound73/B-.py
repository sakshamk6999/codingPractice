for _ in range(int(input())):
    number = int(input())
    inA = list(map(int, input().split()))
    X = int(input())
    sum = 0
    for i in range(number):
        sum += inA[i]
    leftSum = inA[0]
    rightSum = sum - leftSum
    lAns = 1
    rAns = number - 1
    for i in range(1, number):
        if rightSum - inA[i] == leftSum/X:
            if lAns >= rAns - 1:
                # print(l1, r1)
                lAns += 1
                rAns -= 1
                break
            else:
                break
        elif rightSum - inA[i] < leftSum/X:
            break
        else:
            lAns += 1
            rAns -= 1
        leftSum += inA[i]
        rightSum -= inA[i]

    print(lAns, rAns)