for _ in range(int(input())):
    n = int(input())
    matrix = []
    matrix.append(list(input()))
    matrix.append(list(input()))
    pi, pj = 0, -1
    i, j = 0, 0
    # ni, nj = 0, 0
    visited = [[0 for i in range(n)]for i in range(2)]
    while i < 2 and j < n:
        if visited[i][j] == 1:
            break
        visited[i][j] = 1
        if matrix[i][j] == '1' or matrix[i][j] == '2':
            if pi == i:
                j += 1
                pj += 1
            else:
                break
        else:
            if pi == i:
                pi, pj = i, j
                if j < pj:
                    break
                if i == 0:
                    i = 1
                else:
                    i = 0
            else:
                pi, pj = i, j
                j += 1
    if i == 1 and j == n:
        print('YES')
    else:
        print('NO')

