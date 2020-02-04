n = int(input())
if n <= 3:
    print(1)
elif n <= 5:
    print(2)
else:
    if n % 2 == 0:
        print(2)
    else:
        print(3)