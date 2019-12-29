from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    n = 2 * n
    a = list(map(int, input().split()))
    left = a[:n//2]
    right = a[n//2:]
    # print(left)
    minSum = {}
    minSum = defaultdict(lambda : -1, minSum)
    temp = 0
    leftSum = 0
    rightSum = 0
    for i in range(n//2 - 1, -1, -1):
        # print("left", left[i])
        temp += 1 if left[i] == 2 else -1
        rightSum += 1 if right[i] == 2 else -1
        # print("temp is", temp)
        if minSum[temp] == -1:
            minSum[temp] = n//2 - i
    leftSum = temp
    ans = float('inf')
    temp = 0
    # print(minSum)
    if leftSum + rightSum == 0:
        print(0)
    else:
        for i in range(n//2):
            temp += 1 if right[i] == 2 else -1
            remSum = rightSum - temp
            if minSum[leftSum + remSum] != -1:
                ans = min(ans, minSum[leftSum + remSum] + i + 1)
                # print(ans)

        print(ans)