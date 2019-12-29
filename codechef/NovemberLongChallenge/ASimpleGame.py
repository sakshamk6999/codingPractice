from collections import defaultdict
import heapq
try:
    for _ in range(int(input())):
        n = int(input())
        mat = []
        ans = 0
        extreme = defaultdict(list)
        recordL = defaultdict(list)
        recordR = defaultdict(list)
        lHeap = []
        rHeap = []
        for i in range(n):
            s = list(map(int, input().split()))
            mat.append(s[1:])
            extreme[i] = [0, s[0] - 1]
            recordL[mat[i][0]].append(i)
            recordR[mat[i][s[0] - 1]].append(i)
            heapq.heappush(lHeap, -1 * mat[i][0])
            heapq.heappush(rHeap, -1 * mat[i][s[0] - 1])

        while rHeap != [] and lHeap != []:
            t = -1 * heapq.heappop(lHeap)
            # print(t)
            p = recordL[t].pop()
            extreme[p][0] += 1
            ans += t
            # print('ans', ans)
            if extreme[p][1] - extreme[p][0] > 0:
                heapq.heappush(lHeap, -1 * mat[p][extreme[p][0]])
                recordL[mat[p][extreme[p][0]]].append(p)

            t = -1 * heapq.heappop(rHeap)
            p = recordR[t].pop()
            extreme[p][1] -= 1
            if extreme[p][1] - extreme[p][0] > 0:
                heapq.heappush(rHeap, -1 * mat[p][extreme[p][1]])
                recordR[mat[p][extreme[p][1]]].append(p)

        if rHeap == []:
            lHeap.sort()
            for i in range(1, len(lHeap), 2):
                ans += -1 * lHeap[i]
        else:
            rHeap.sort()
            for i in range(0, len(rHeap), 2):
                ans += -1 *rHeap[i]

        print(ans)
except:
    exit()