def converToBinary(n):
    ans = []
    while n > 0:
        ans.append(n%2)
        n = n // 2
    ans.reverse()
    return ans

for _ in range(int(input())):
    l, r = map(int, input().split())
    t1 = converToBinary(l)
    t1.reverse()
    t2 = converToBinary(r)
    i = len(t2)
    j = len(t1)
    while i > j:
        j += 1
        t1.append(0)
    t1.reverse()
    i -= 1
    ans = l | r
    p = 0

    while l <= r and i >= 0:
        if t1[i] == 0:
            if t2[i] == 0:
                if l + 2**p <= r:
                    temp = 2**p
                    ans += temp
                    l += temp

                else:
                    break
        i -= 1
        p += 1

    print(ans)

