from collections import defaultdict
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

a_set = list(set(a))
b_set = list(set(b))
rec = {}
rec = defaultdict(lambda : 0, rec)
rec_b = {}
rec_b = defaultdict(lambda : 0, rec_b)
for i in range(n):
    rec[a[i]] += 1
    rec_b[b[i]] += 1

rec_t = defaultdict(list)
rec_m = defaultdict(list)
mList = set()
for i in range(len(a_set)):
    for j in range(len(b_set)):
        if rec[a_set[i]] == rec_b[b_set[i]]:
            rec_t[a_set[i]].append([(b_set[i] - a_set[i]) % m, b_set[i]])
            mList.add((b_set[i] - a_set[i]) % m)
            rec_m[(b_set[i] - a_set[i]) % m].append(b_set[i])

possibleM = []
for i in mList:
    if len(set(rec_m[i])) == len(rec_m[i]):
        possibleM.append(i)

possibleM.sort()
print(possibleM[0])






