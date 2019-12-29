def getPath(i, j, x, y, pathList, tempPath, mat, times):
    if i == x and j == y:
        pathList.append(tempPath.copy())
        for i in tempPath:
            times[i[0]][i[1]] += 1
        return
    else:
        if mat[i][j] == '#':
            return
        else:
            tempPath.append([i, j])
            if i < x:
                getPath(i + 1, j, x, y, pathList, tempPath, mat, times)
            if j < y:
                getPath(i, j + 1, x, y, pathList, tempPath, mat, times)
            tempPath.pop()
            return

n, m = map(int, input().split())

mat = []

for i in range(n):
    mat.append(list(input()))

pathList = []
tempPath = []
times = [[0 for i in range(m)] for i in range(n)]
getPath(0, 0, n - 1, m - 1, pathList, tempPath, mat, times)
t = len(pathList)
if t == 0:
    print(0)
else:
    flag = 2
    # for i in times:
    #     print(i)
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            if times[i][j] == t:
                flag = 1
                break
        if flag == 1:
            break
    print(flag)

