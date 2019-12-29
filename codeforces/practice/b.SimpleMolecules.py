a, b, c = map(int, input().split())
x = (a + c - b)//2
z = (b + c - a)//2
y = (a + b - c)//2

if x < 0 or y < 0 or z < 0:
    print('Impossible')
else:
    print(y, z, x)