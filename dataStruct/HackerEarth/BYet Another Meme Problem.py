for _ in range(int(input())):
    a, b = map(int, input().split())
    n_a = 0
    temp = 0
    while temp < a:
        temp += 9
        if temp <= a:
            n_a += 1
            temp *= 10
        else:
            break

    n_b = 0
    temp = 0
    while temp < b:
        temp += 9
        if temp <= b:
            n_b += 1
            temp *= 10
        else:
            break
    print(n_b*a)
    # print(n_b*a + n_a*b - n_a ** 2)