def find(parent, i):
    if parent[i] == -1:
        return i
    return find(parent, parent[i])

for t in range(int(input())):
    n, m = map(int, input().split())
    vertices = [0 for i in range(n)]
    # unique = 0
    parent = [-1 for i in range(n)]
    ans = 0
    num = n
    for _ in range(m):
        v, e = map(int, input().split())
        j = find(parent, v - 1)
        k = find(parent, e - 1)
        if j != k:
            parent[e - 1] = v - 1
            ans += 1
            num -= 1

    # ans = (unique - 1) + (n - unique)*2
    ans += (num - 1)*2
    if n == 1:
        ans = 0
    print("Case #" + str(t + 1) + ":", ans)