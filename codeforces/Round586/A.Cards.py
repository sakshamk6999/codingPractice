n = int(input())
a = list(input())
z = 0
o = 0
for i in a:
    if i == 'z':
        z += 1
    elif i == 'o':
        o += 1

for i in range(o - z):
    print(1, end=" ")
for i in range(z):
    print(0, end=' ')
print('')