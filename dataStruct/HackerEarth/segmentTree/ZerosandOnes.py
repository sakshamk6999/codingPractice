from math import log
def makeSegTree(a, t, l, r, i):
    # print(l, i)
    if l == r:
        t[i] = a[l]
    else:
        m = (l + r)//2
        makeSegTree(a, t, l, m, 2*i + 1)
        makeSegTree(a, t, m + 1, r, 2*i + 2)
        t[i] = t[2*i + 1] + t[2*i + 2]

def update(t, l, r, i, idx):
    if l == r:
        t[i] = 0
    else:
        mid = (l + r)//2
        if l <= idx and idx <= mid:
            update(t, l, mid, 2*i + 1, idx)
        else:
            update(t, mid + 1, r, 2*i + 2, idx)

        t[i] = t[2*i + 1] + t[2*i + 2]

def getKthOne(t, l, r, i, k):
    # print(l, r)
    if k > t[i]:
        return -2
    if t[i] == k:
        return r
    mid = (l + r)//2
    if k <= t[2*i + 1]:
        return getKthOne(t, l, mid, 2*i + 1, k)

    return getKthOne(t, mid + 1, r, 2*i + 2, k - t[2*i + 1])

n = int(input())
t = log(n, 2)
# print(t)
if t != int(t):
    t += 1
a = [1 for i in range(n)]
tree = [0 for i in range(2**int(t + 1) - 1)]
# print(len(tree))
# print(tree)
makeSegTree(a, tree, 0, n - 1, 0)
# print(tree)
for i in range(int(input())):
    x, y = map(int, input().split())
    if x == 0:
        update(tree, 0, n - 1, 0, y - 1)
    else:
        print(getKthOne(tree, 0, n - 1, 0, y) + 1)