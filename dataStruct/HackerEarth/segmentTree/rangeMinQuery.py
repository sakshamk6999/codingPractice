import math
def makeSegTree(a, t, l, r, i):
    if l == r:
        t[i] = a[l]
    else:
        mid = (l + r)//2
        makeSegTree(a, t, l, mid, 2*i + 1)
        makeSegTree(a, t, mid + 1, r, 2*i + 2)
        t[i] = min(t[2*i + 1], t[2*i + 2])

def updateSegTree(a, t, l, r, i, val, idx):
    if l == r:
        t[i] = val
        a[idx] = val
    else:
        mid = (l + r)//2
        if l <= idx and idx <= mid:
            updateSegTree(a, t, l, mid, 2*i + 1, val, idx)
        else:
            updateSegTree(a, t, mid + 1, r, 2*i + 2, val, idx)

        t[i] = min(t[2*i + 1], t[2*i + 2])

def query(t, s, e, l, r, i):
    # print(s, e, i)
    if r < s or l > e:
        return float('inf')
    elif l <= s and r >= e:
        # print(i)
        return t[i]
    else:
        mid = (s + e)//2
        return min(query(t, s, mid, l, r, 2*i + 1), query(t, mid + 1, e, l, r, 2*i + 2))

n, q = map(int, input().split())
a = list(map(int, input().split()))
temp = math.log(n, 2)
if temp != int(temp):
    temp += 1
t = [0 for i in range(2*int(temp) - 1)]
makeSegTree(a, t, 0, n - 1, 0)
# print(t)
for i in range(q):
    ty, l, r = input().split()
    l = int(l)
    r = int(r)
    if ty == 'q':
        print(query(t, 0, n - 1, l - 1, r - 1, 0))
    else:
        updateSegTree(a, t, 0, n - 1, 0, r, l - 1)
        # print(t)