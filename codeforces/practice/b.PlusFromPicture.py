h, w = map(int, input().split())
matrix = []
for _ in range(h):
    matrix.append(list(input()))

count = 0
for i in range(h):
    for j in range(w):
        if matrix[i][j] == '*' and ((i + 1 < h) and matrix[i + 1][j] == '*') and ((j + 1 < w) and matrix[i][j + 1] == '*') and ((i - 1 >= 0) and matrix[i - 1][j] == '*') and ((j - 1 >= 0) and matrix[i][j - 1] == '*'):
            count += 1
            if count > 1:
                break
    if count > 1:
        break

if count == 1:
    print('YES')
else:
    print('NO')
