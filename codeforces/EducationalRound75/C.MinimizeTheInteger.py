for _ in range(int(input())):
    s = list(map(int, list(input())))
    even = []
    odd = []
    for i in s:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    # print(even)
    # print(odd)
    i = 0
    j = 0
    while i < len(even) and j < len(odd):
        if even[i] < odd[j]:
            i += 1
            print(even[i - 1], end='')
        else:
            j += 1
            print(odd[j - 1], end='')

    while i < len(even):
        i += 1
        print(even[i - 1], end='')

    while j < len(odd):
        j += 1
        print(odd[j - 1], end='')

    print('')