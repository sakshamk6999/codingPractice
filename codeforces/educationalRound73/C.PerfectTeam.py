for _ in range(int(input())):
    ans = 0
    c, m, x = map(int, input().split())
    ans += min(min(c, m), (c + m + x)//3)
    print(ans)
    # c -= ans
    # m -= ans
    # x -= ans
    # if c == 0 or m == 0:
    #     print(ans)
    # else:
    #     if c > m:
    #         if c//2 > m:
    #             ans += m
    #         else:
    #             ans += c // 2
    #             if c % 2 == 1:
    #                 if m - c // 2 >= 2:
    #                     ans += 1
    #     else:
    #         if m//2 > c:
    #             ans += c
    #         else:
    #             ans += m // 2
    #             if m % 2 == 1:
    #                 if c - m//2 >= 2:
    #                     ans += 1
    #     print(ans)