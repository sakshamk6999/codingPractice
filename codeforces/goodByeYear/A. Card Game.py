for _ in range(int(input())):
    n, a, b = map(int, input().split())
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    if n in first:
        print('YES')
    else:
        print('NO')