for _ in range(int(input())):
    a, b, c = sorted(list(map(int, input().split())))
    if a == b and b == c:
        print(0)
    elif a == b or b == c:
        if abs(a - b) + abs(b - c) + abs(a - c) == 2:
            print(0)
        else:
            print(abs(a - b) + abs(b - c) + abs(a - c) - 4)
    else:
        print(abs(a - b) + abs(b - c) + abs(a - c) - 4)