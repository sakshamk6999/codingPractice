t = 10**9 + 7
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    s_a = set(a[:2*n - 2])
    f = {}
    if a[2*n - 1] == a[2*n - 2]:
        p = 1
        rec = {}
        for i in range(2*n - 2):
            if rec.get(a[i], 0) == 0:
                rec[a[i]] = 1
            else:
                rec[a[i]] += 1
        ans = 0
        for i in s_a:
            if f.get(i, 0) != 0:
                continue
            if a[2*n - 1] - i == i:
                temp = (rec.get(i, 0) % t)
            else:
                temp = ((rec.get(i, 0)%t) * (rec.get(a[2*n - 1] - i, 0)%t)) % t
            if temp == 0:
                ans = -1
                break
            ans += temp
            ans = ans % t
            f[i] = 1

        if ans == -1:
            print(0)
        elif ans == 0:
            print(1)
        else:
            print(ans % t)

    else:
        print(0)