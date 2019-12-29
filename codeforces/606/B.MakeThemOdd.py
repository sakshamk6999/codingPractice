from collections import defaultdict
import heapq
for _ in range(int(input())):
    n = int(input())
    rec = {}
    rec = defaultdict(lambda : 0, rec)

    a = sorted(list(map(int, input().split())))
    e = []
    l = 0
    for i in a:
        if i % 2 == 0 and rec[-1 * i] == 0:
            e.append(-1 * i)
            rec[-1 * i] = 1
            l += 1

    heapq.heapify(e)
    ans = 0

    while l > 0:
        # print(e)
        ans += 1
        temp = heapq.heappop(e)
        # print("temp", -1 * temp)

        rec[temp] = 0
        temp = (-1 * temp) // 2
        if temp % 2 == 0:
            if rec[-1 * temp] == 1:
                # print("temp is in", - 1 * temp)
                l -= 1
            else:
                rec[-1 * temp] = 1
                heapq.heappush(e, -1 * temp)
        else:
            l -= 1

    print(ans)