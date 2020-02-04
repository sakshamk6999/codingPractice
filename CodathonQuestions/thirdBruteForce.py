from itertools import permutations
t = 10**9 + 7

def brute(a, i, m, n, s, l, ans):
    # print(i, n, s)
    if i >= l:
        return 0
    if n == 0:
        # print('yes')
        if s % m == 0:
            # print(ans)
            return len(set(list(permutations(ans)))) % t
        else:
            return 0
    if n < 0:
        return 0
    temp = ans.copy()
    temp.append(a[i])
    return ((brute(a, i, m, n - 1, s + a[i], l, temp.copy()) % t)
            + (brute(a, i + 1, m, n, s, l, ans.copy()) % t)) % t

n, m, l = map(int, input().split())
a = list(map(int, input().split()))

ans = []
print(brute(a, 0, m, n, 0, l, ans) % t)