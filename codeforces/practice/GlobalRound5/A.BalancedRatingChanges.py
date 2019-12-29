# from
n = int(input())
even = []
odd = []
sumEven = 0
sumOdd = 0
ans = []
for i in range(n):
    t = int(input())
    if abs(t) % 2 == 0:
        even.append(i)
        sumEven += t//2
    else:
        odd.append(i)
        sumOdd += t//2
    ans.append(t//2)

# d = sumEven - sumOdd


# if d <= 0:
#     k = 0
#     for i in range(len(odd)):
#         if k >= d:
#             break
#         if ans[odd[i]] < 0:
#             ans[odd[i]] += 1
#             k += 1
# else:
#     for i in range(d):
#         ans[odd[i]] += 1
d = sumEven + sumOdd
k = 0
for i in odd:
    if k >= abs(d):
        break
    ans[i] += 1
    k += 1


for i in ans:
    print(i)