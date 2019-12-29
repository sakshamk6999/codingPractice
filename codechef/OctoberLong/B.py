for _ in range(int(input())):
    n = int(input())
    r = list(map(int, list(input())))
    if r[0] == 1 or r[n - 1] == 1:
        print(2 * n)
    else:
        l = n 
        for i in range(n):
            if r[i] == 1:
                l = i
                break
        right = -1
        for i in range(n - 1, -1, -1):
            if r[i] == 1:
                right = i
                break

        print(max(n + sum(r), 2 * (n - l), 2 * (right + 1)))