from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    rec = defaultdict(list)
    for i in range(n):
        a = list(input())
        rec[i] = [0, 0]
        for j in range(n//2):
            rec[i][0] += int(a[j])
        for j in range(n//2, n):
            rec[i][1] += int(a[j])
    initial = 0
    for i in range(n):
        initial += rec[i][0]
    for i in range(n):
        initial -= rec[i][1]

    minVal = abs(initial)
    for i in range(n):
        minVal = min(minVal, abs(initial - 2 * rec[i][0] + 2 * rec[i][1]))
    print(minVal)