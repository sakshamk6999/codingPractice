import math
def constructTree(input, segTree, low, high, pos):
    # print(low, high, pos)
    if low == high:
        # print(pos)
        segTree[pos] = input[low]
        return

    mid = (low + high)//2
    constructTree(input, segTree, low, mid, 2*pos + 1)
    constructTree(input, segTree, mid + 1, high, 2*pos + 2)
    segTree[pos] = segTree[2*pos + 1] + segTree[2*pos + 2]

def rangeQuery(segTree, qlow, qhigh, low, high, pos):
    if qlow <= low and qhigh >= high:
        return segTree[pos]
    if qlow > high or qhigh < low:
        return 0
    mid = (low + high)//2
    return rangeQuery(segTree, qlow, qhigh, low, mid, 2 * pos + 1) + rangeQuery(segTree, qlow,
                                                                                qhigh, mid + 1,
                                                                                high, 2 * pos + 2)

for _  in range(int(input())):
    s = list(map(int, input().split()))
    n = 2 * (2**(math.ceil(math.log(len(s), 2)))) - 1
    # print("size is ", n)
    segTree = [0 for i in range(n)]

    constructTree(s, segTree, 0, len(s) - 1, 0)
    # print(segTree)
    q = int(input())
    for i in range(q):
        l, r = map(int, input().split())
        print(rangeQuery(segTree, l, r, 0, len(s) - 1, 0))


