a = list(input())
n = len(a)
value = 0
for i in range(n - 1, -1, -1):
    if a[i] == '1':
        value += 2**(n - 1 - i)
count = 0
while value > 0:
    count += 1
    value = value // 4

print(count)