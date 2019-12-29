n = int(input())
arr1 = 'WB'*(n//2)
if n % 2 != 0:
    arr1 += 'W'
arr2 = 'BW' * (n // 2)
if n % 2 != 0:
    arr2 += 'B'
flag = 0
for i in range(n):
    if flag == 0:
        print(arr1)
        flag = 1
    else:
        flag = 0
        print(arr2)