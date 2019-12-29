n, p, w, d = map(int, input().split())
r = p % w
if r == 0 and p//w <= n:
    print(p//w, 0, n - p//w)
else:
    rd = r % d
    if rd % w == 0:
        x = p//w - (rd//w)
        y = (rd + r)//d
        print(x, y, n - x - y)
    else:
        print(-1)