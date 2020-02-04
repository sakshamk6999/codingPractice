n = int(input())
a = list(map(int, input().split()))
s = sum(a)
# n = len(a)
three = 0
two = 0
if s % 3 == 0:
    #beginning
    temp = 0
    i = 0
    while i < n and temp != s // 3:
        temp += a[i]
        i += 1
    #count zeros after it
    i += 1
    x = 0
    while i < n and a[i] == 0:
        x += 1
        i += 1

    y = 0
    temp = 0
    while i < n and temp != s // 3:
        temp += a[i]
        i += 1

    # count zeros after it
    i += 1
    while i < n and a[i] == 0:
        y += 1
        i += 1

    if temp == s // 3:
        three = (2**x)*(2**y)

print(three)