n = int(input())

mat = [[0 for i in range(n)]for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == 0:
            if j == 0:
                mat[i][j] = n
            else:
                if j % 2 == 1:
                    mat[i][j] = mat[i][j - 1] + 1
                else:
                    mat[i][j] = mat[i][j - 1] + 2 * n - 1
        else:
            if j % 2 == 1:
                mat[i][j] = mat[i - 1][j] + 1
            else:
                mat[i][j] = mat[i - 1][j] - 1

for i in mat:
    for j in i:
        print(j, end= ' ')
    print('')


