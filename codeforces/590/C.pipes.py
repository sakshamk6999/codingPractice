for _ in range(int(input())):
    n = int(input())
    mat = []
    mat.append(list(map(int, list(input()))))
    mat.append(list(map(int, list(input()))))
    visited = [[0 for i in range(n)] for i in range(2)]
    water = [0, -1]
    next = [0, 0]
    flag = 1
    while next != [1, n] and water != [1, n]:
        # visited[water[0]][water[1]] = 1
        print(water, next)

        if mat[next[0]][next[1]] == 1 or mat[next[0]][next[1]] ==2 and visited[next[0]][next[1]] == 0:
            visited[next[0]][next[1]] = 1
            if water[0] == next[0]:
                if water[1] < next[1]:
                    next = [next[0], next[1] + 1]
                    water = [water[0], water[1] + 1]
                else:
                    next = [next[0], next[1] - 1]
                    water = [water[0], water[1] - 1]
            elif water[1] == next[1]:
                flag = 0
                break

        if mat[next[0]][next[1]] == 3 or mat[next[0]][next[1]] == 4 or mat[next[0]][next[1]] == 5 or mat[next[0]][next[1]] == 6 and visited[next[0]][next[1]] == 0:
            visited[next[0]][next[1]] = 1
            if water[0] == next[0]:
                if water[0] == 0:
                    if water[1] < next[1]:
                        water = [water[0], water[1] + 1]
                    else:
                        water = [water[0], water[1] - 1]
                    next = [next[0] + 1, next[1]]
                else:
                    if water[1] < next[1]:
                        water = [water[0], water[1] + 1]
                    else:
                        water = [water[0], water[1] - 1]
                    next = [next[0] - 1, next[1]]
            else:
                if water[0] == 0:
                    water = [water[0] + 1, water[1]]

                else:
                    water = [water[0] - 1, water[1]]

                next = [next[0], next[1] + 1]
        else:
            flag = 0
            break
    if flag == 1:
        print('YES')
    else:
        print('NO')