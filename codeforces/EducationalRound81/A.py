from collections import defaultdict
rec = defaultdict(int)
rec[2] = 1
rec[3] = 7
rec[4] = 4
rec[5] = 5
rec[6] = 9
rec[7] = 8
for _ in range(int(input())):
    n = int(input())
    no = n // 2
    n = n - 2*(n//2)
    if n < 2:
        no -= 1
        n += 2
    print(str(rec[n]) + '1'*no)
