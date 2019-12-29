from collections import defaultdict
for _ in range(int(input())):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    rec = defaultdict(int)
    ans = 0
    for i in range(d):
        if rec.get(a[i], 0) == 0:
            ans += 1
            rec[a[i]] = 1
        else:
            rec[a[i]] += 1
    # print('ans is', ans)
    temp = ans
    for i in range(1, n - d + 1):
        # print('temp', temp)
        rec[a[i - 1]] -= 1
        if rec[a[i - 1]] == 0:
            temp -= 1
        if rec.get(a[i + d - 1], 0) == 0:
            temp += 1
            rec[a[i + d - 1]] = 1
        else:
            rec[a[i + d - 1]] += 1

        ans = min(temp, ans)

    print(ans)