import math

def constructTree(tree, arr, low, high, pos, op):
    # print(low, high, pos, op)
    if low == high:
        tree[pos] = arr[low]
        return
    mid = (low + high)//2
    constructTree(tree, arr, low, mid, 2 * pos + 1, -1 * op)
    constructTree(tree, arr, mid + 1, high, 2 * pos + 2, -1 * op)
    tree[pos] = tree[2 * pos + 1] | tree[2 * pos + 2] if op == 1 else tree[2 * pos + 1] ^ tree[2 * pos + 2]

def updateTree(tree, pos, op):
    if pos == 0:
        return tree[2 * pos + 1] | tree[2 * pos + 2] if op == 1 else tree[2 * pos + 1] ^ tree[2 * pos + 2]
    prev = tree[pos]
    tree[pos] = tree[2 * pos + 1] | tree[2 * pos + 2] if op == 1 else tree[2 * pos + 1] ^ tree[2 * pos + 2]
    if pos % 2 == 0:
        ans = updateTree(tree, (pos//2) - 1, -1 * op)
    else:
        ans = updateTree(tree, pos//2, -1 * op)
    # tree[pos] = prev
    return ans

def updateTree2(tree, pos, child, b, op):
    if pos == child // 2:
        if pos % 2 == 0:
            if op == 1:
                if pos > 0:
                    return updateTree2(tree, pos // 2 - 1, pos, b | tree[2 *pos + 2], -1 * op)
                else:
                    return b | tree[2 * pos + 2]
            else:
                if pos > 0:
                    return updateTree2(tree, pos // 2 - 1, pos, b ^ tree[2 * pos + 2], -1 * op)
                else:
                    return b ^ tree[2 * pos + 2]
        else:
            if op == 1:
                if pos > 0:
                    return updateTree2(tree, pos // 2, pos, b | tree[2 *pos + 2], -1 * op)
                else:
                    return b | tree[2 * pos + 2]
            else:
                if pos > 0:
                    return updateTree2(tree, pos // 2, pos, b ^ tree[2 * pos + 2], -1 * op)
                else:
                    return b ^ tree[2 * pos + 2]

    else:
        if pos % 2 == 0:
            if op == 1:
                if pos > 0:
                    return updateTree2(tree, pos // 2 - 1, pos, b | tree[2 * pos + 1], -1 * op)
                else:
                    return b | tree[2 * pos + 1]
            else:
                if pos > 0:
                    return updateTree2(tree, pos // 2 - 1, pos, b ^ tree[2 * pos + 1], -1 * op)
                else:
                    return b ^ tree[2 * pos + 1]
        else:
            if op == 1:
                if pos > 0:
                    return updateTree2(tree, pos // 2, pos, b | tree[2 * pos + 1], -1 * op)
                else:
                    return b | tree[2 * pos + 1]
            else:
                if pos > 0:
                    return updateTree2(tree, pos // 2, pos, b ^ tree[2 * pos + 1], -1 * op)
                else:
                    return b ^ tree[2 * pos + 1]

p, m = map(int, input().split())
a = list(map(int, input().split()))
n = 2 ** p
tree = [0 for i in range(2**(p + 1) - 1)]
# print(tree)
# print(len(tree))
if p % 2 == 0:
    constructTree(tree, a, 0, n - 1, 0, -1)
else:
    constructTree(tree, a, 0, n - 1, 0, 1)
# print(tree)
diff = 2**p - 1
for i in range(m):
    # print(tree)
    p, b = map(int, input().split())
    t = p + diff - 1
    prev = tree[t]
    tree[t] = b
    if t % 2 == 0:
        # print(updateTree2(tree, t//2 - 1, t, b, 1))
        print(updateTree(tree, t//2 - 1, 1))
    else:
        # print(updateTree2(tree, t//2, t, b, 1))
        print(updateTree(tree, t//2, 1))
    # tree[t] = prev

    # print(tree[0])