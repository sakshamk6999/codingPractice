for _ in range(int(input())):
    a, b, c = sorted(list(map(int, input().split())), reverse=True)
    if a > b + c + 1:
        print("No")
    else:
        print("Yes")