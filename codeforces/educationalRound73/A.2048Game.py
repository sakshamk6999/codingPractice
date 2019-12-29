for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    d = {}
    if 2048 in a:
        print("Yes")
        continue
    for i in a:
        if i <= 2048:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    # print(d)
    k = 0
    m = 0
    p = 0
    req = {1024 : 2, 512 : 4, 256 : 8, 128 : 16, 64 : 32, 32 : 64, 16 : 128, 8 : 256, 4 : 512, 2 : 1024}
    r = [2**i for i in range(12)]
    for i in range(12):
        if 2**(11-i) in d:
            r[i] -= d[2**(11-i)]
            m = d[2**(11-i)]
            if i != 11:
                for j in range(i+1,len(r)):
                    p = 2*m
                    r[j] -= p
                    m = p
            for j in r:
                if j <= 0:
                    print("Yes")
                    k = 1
                    break
            if k == 1:
                break
    if k == 0:
        print("No")