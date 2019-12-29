from collections import defaultdict
n = int(input())
s = list(map(int, list(input())))
rec = defaultdict(list)
rec2 = defaultdict(int)
f = defaultdict(int)
for i in range(10):
    rec[i] = []
    f[i] = 0

for i in range(n):
    rec[s[i]].append(i)
    rec2[i] = s[i]
    f[s[i]] += 1

temp = []
for i in range(10):
    if f[i] % 2 != 0:
        temp.extend(rec[i])
# print(temp)
temp.sort()
t = f.copy()
#left to right
left = len(temp) - 1
right = left

for i in range(len(temp)):
    if t[rec2[temp[i]]] == 1:
        left = i
        break
    else:
        t[rec2[temp[i]]] -= 1

for i in range(len(temp) - 1, left - 1, -1):
    if t[rec2[temp[i]]] == 1:
        right = i
        break
    else:
        t[rec2[temp[i]]] -= 1
# print(left, right)
ans = temp[right] - temp[left]

#right to left
right = len(temp) - 1
left = right
t = f.copy()
for i in range(len(temp) - 1, -1, -1):
    if t[rec2[temp[i]]] == 1:
        right = i
        break
    else:
        t[rec2[temp[i]]] -= 1

for i in range(right + 1):
    if t[rec2[temp[i]]] == 1:
        left = i
        break
    else:
        t[rec2[temp[i]]] -= 1
# print(left, right)
ans = min(ans, temp[right] - temp[left])

print(ans)
