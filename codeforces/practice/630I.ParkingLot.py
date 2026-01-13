n = int(input())
ans = 0
for j in range(n - 1):
    temp = 1
    left = j
    right = 2*n - 2 - left - n

    if j == 1:
        temp *= 3
    elif j > 1:
        temp *= 3 * (4**(left - 1))
    
    temp *= 4

    if right == 1:
        temp *= 3
    elif right > 1:
        temp *= 3 * (4**(right - 1))
    ans += temp
print(ans)