import ct
s = list(input())
n = len(s)
q = int(input())
mat = [[0 for i in range(n)]for i in range(26)]
rec = {}
rec['a'] = 0
rec['b'] = 1
rec['c'] = 2
rec['d'] = 3
rec['e'] = 4
rec['f'] = 5
rec['g'] = 6
rec['h'] = 7
rec['i'] = 8
rec['j'] = 9
rec['k'] = 10
rec['l'] = 11
rec['m'] = 12
rec['n'] = 13
rec['o'] = 14
rec['p'] = 15
rec['q'] = 16
rec['r'] = 17
rec['s'] = 18
rec['t'] = 19
rec['u'] = 20
rec['v'] = 21
rec['w'] = 22
rec['x'] = 23
rec['y'] = 24
rec['z'] = 25

for i in range(n):
    mat[rec[s[i]]][i] = 1

for _ in range(q):
    t, l, r = map(int, input().split())
    if t == '1':
