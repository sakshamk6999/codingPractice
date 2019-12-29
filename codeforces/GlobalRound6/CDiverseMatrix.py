r, c = map(int, input().split())
mat = [[1 for i in range(r)]for i in range(c)]
if r == 1 and c == 1:
    print(0)
elif r == 1:
    mat = [0 for i in range(c)]
    for i in range(c):
        print(i + 2, end=' ')
    print('')
else:
    for i in range(r):
        mat[0][i] = i + 2
    t = r + 2
    for i in range(1, c):
        for j in range(r):
            mat[i][j] = mat[0][j] * t
        t += 1
    for i in range(r):
        for j in range(c):
            print(mat[j][i], end=' ')
        print('')