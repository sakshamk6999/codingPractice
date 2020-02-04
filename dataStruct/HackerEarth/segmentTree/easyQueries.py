import math
def makeSegTree(a, t1, t2, i, l, r):
    if l == r:
        if a[l] == 1:
            t1[i] = l
            t2[i] = l
        else:
            t1[i] = -1
            t2[i] = -1
    else:
        mid = (l + r)//2
        makeSegTree(a, t1, t2, 2*i + 1, l, mid)
        makeSegTree(a, t1, t2, 2*i + 2, mid + 1, r)
        t1[i] = max(t1[2*i + 1], t1[2*i + 2])
        t2[i] = min(t2[2*i + 1], t2[2*i + 2])

def updateSegTree(a, t1, t2, x, i, l, r):
    if l == r:
        a[x] = 1
        t1[i] = l
        t2[i] = l
    else:
        mid = (l + r) // 2
        if x >= l and x <= mid:
            updateSegTree(a, t1, t2, x, 2*i + 1, l, mid)
        else:
            updateSegTree(a, t1, t2, x, 2*i + 2, mid + 1, r)
        t1[i] = max(t1[2 * i + 1], t1[2 * i + 2])
        t2[i] = min(t2[2 * i + 1], t2[2 * i + 2])

def query(t1, t2, s, e, l, r, i):
    if l <= s and r >= e:
        return [t1[i], t2[i]]
    elif l > e or r < s:
        return [-1, float('inf')]
    else:
        mid = (s + e)//2
        temp = query(t1, t2, s, mid, l, r, 2*i + 1)
        temp2 = query(t1, t2, mid + 1, e, l, r, 2*i + 2)
        return [max(temp[0], temp2[0]), min(temp[1], temp2[1])]

n, q = map(int, input().split())
a = list(map(int, input().split()))
r = math.log(n, 2)
if r != int(r):
    r += 1

t1 = [0 for i in range(2**int(r + 1) - 1)]
t2 = [0 for i in range(2**int(r + 1) - 1)]

makeSegTree(a, t1, t2, 0, 0, n - 1)

for _ in range(q):
    type, i = map(int, input().split())
    if type == 0:
        if i != 0 and i != n - 1:
            print(query(t1, t2, 0, n - 1, 0, i - 1, 0)[0], query(t1, t2, 0, n - 1, i + 1, n, 0)[1])
        elif i == 0:
            print(-1, query(t1, t2, 0, n - 1, i + 1, n, 0)[1])
        else:
            print(query(t1, t2, 0, n - 1, 0, i - 1, 0)[0], -1)
    else:
        updateSegTree(a, t1, t2, i - 1, 0, 0, n - 1)
