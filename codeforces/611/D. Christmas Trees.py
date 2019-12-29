n, m = map(int, input().split())
x = list(map(int, input().split()))
y = []
occ = {}
dis = {}
for i in x:
    occ[i] = 1
d = 0
ans = 0
while m > 0:
    d += 1
    j = 0
    while j < n:
        if occ.get(x[j] - d, 0) == 0:
            occ[x[j] - d] = 1
            y.append(x[j] - d)
            ans += d
            # if dis.get(d, 0) == 0:
            #     dis[d] = 1
            # else:
            #     dis[d] += 1
            if m > 0:
                m -= 1
            else:
                break
        if m == 0:
            break
        if occ.get(x[j] + d, 0) == 0:
            occ[x[j] + d] = 1
            y.append(x[j] + d)
            ans += d
            # if dis.get(d, 0) == 0:
            #     dis[d] = 1
            # else:
            #     dis[d] += 1
            #
            if m > 0:
                m -= 1
            else:
                break
        if m == 0:
            break
        j += 1


print(ans)
for i in y:
    print(i, end=' ')
print('')