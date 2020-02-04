import random
i = 10
for T in range(10):
    fi = open('./testcasesThird/input' + str(3 + T) + '.txt', 'w')
    fo = open('./testcasesThird/output' + str(3 + T) + '.txt', 'w')
    n = min(i, 10**5)
    i *= 10
    m = random.randint(1, 10)
    l = 0
    a = []
    for j in range(m):
        t = random.randint(0, 10**5 - l)
        l += t
        a.extend([j] * t)
    fi.write(str(n) + ' ' + str(m) + ' ' + str(l))
    fi.write('\n' + ' '.join(list(map(str, a))))

    dp = [[0 for i in range(n)] for i in range(m)]
    t = 10 ** 9 + 7
    for j in a:
        dp[j % m][0] += 1

    for p in range(1, n):
        for j in range(m):
            for k in range(m):
                dp[j][p] += (dp[k][p - 1] * dp[(j - k) % m][0]) % t
                dp[j][p] = dp[j][p] % t
    fo.write(str(dp[0][n - 1] % t))