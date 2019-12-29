for _ in range(int(input())):
    n = int(input())
    l = 0
    digits = []
    while n != 0:
        digits.append(str(n%10))
        n = n//10
        l += 1
    digits.reverse()

    ans = float('inf')

    for i in range(l):
        ans = min(ans, int(''.join(digits[:i]) + ''.join(digits[i + 1:])))

    print(ans)
