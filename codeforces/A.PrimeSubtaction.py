for i in range(int(input())):
    n, m = map(int, input().split())
    if n - m > 1:
        print("YES")
    else:
        print('NO')
