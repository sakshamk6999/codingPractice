from math import log
def decToBinary(d):
    ans = 0
    while d > 0:
        ans += d % 2
        d = d // 2
    return ans

def makeSegTree(a, t, l, r, i):
    if l == r:
        t[i] = a[l]
    else:
        mid = (l + r)//2
        makeSegTree(a, t, l, mid, 2*i + 1)
        makeSegTree(a, t, mid + 1, r, 2*i + 2)
        t[i] = t[2*i + 1] + t[2*i + 2]

def updateSegTree(a, t, x, s, e, i, type):
    if s == e:
        if type == 1:
            t[i] += 1
            a[x] = a[x] * 2 + 1
        else:
            if a[x] % 2 != 0:
                t[i] -= 1
            a[x] = a[x]//2
    else:
        mid = (s + e)//2
        #left
        if x <= mid and x >= s:
            updateSegTree(a, t, x, s, mid, 2*i + 1, type)
        else:
            updateSegTree(a, t, x, mid + 1, e, 2*i + 2, type)

        t[i] = t[2*i + 1] + t[2*i + 2]

def query(t, l, r, x, y, i):
    if x > r or y < l:
        return 0
    elif x <= l and y >= r:
        return t[i]
    else:
        mid = (l + r)//2
        return query(t, l, mid, x, y, 2*i + 1) + query(t, mid + 1, r, x, y, 2*i + 2)

n, q = map(int, input().split())
po = log(n, 2)
if po != int(po):
    po += 1
a = [0 for i in range(n)]
t = [0 for i in range(2**(int(po) + 1) - 1)]
lazy = [0 for i in range(2**(int(po) + 1) - 1)]
# makeSegTree(a, t, 0, n - 1, 0)
for i in range(q):
    que = list(map(int, input().split()))
    if len(que) == 2:
        updateSegTree(a, t, que[1] - 1, 0, n - 1, 0, que[0])
    else:
        print(query(t, 0, n - 1, que[1] - 1, que[2] - 1, 0))

