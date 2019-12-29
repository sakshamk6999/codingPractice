from collections import defaultdict
for _ in range(int(input())):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    # rec = defaultdict(list)
    ans = 0
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         if a[j] < a[i]:
    #             rec[i].append(j)
    #             ans += 1

    # print('ans', ans)
    for qr in range(q):
        # temp = ans
        ans = 0
        k = int(input())
        # for i in range(n):
        #     for j in rec[i]:
        #         if a[j] ^ k >= a[i] ^ k:
        #             temp -= 1
        b = [a[i] ^ k for i in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if b[j] < b[i]:
                    # rec[i].append(j)
                    ans += 1
        print(ans)