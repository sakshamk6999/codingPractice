def numberOfGoodStrings(s, n):
    number = 0
    value = 0
    for i in range(n):
        for j in range(i, n):
            if i == j:
                value = s[j]
            else:
                value = value * 2 + s[j]

            if value == j - i + 1:
                number += 1
        value = 0
    return number

for _ in range(int(input())):
    s = list(map(int, list(input())))
    n = len(s)
    print(numberOfGoodStrings(s, n))

