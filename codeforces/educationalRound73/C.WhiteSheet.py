x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

#for 1st sheet
if y3 >= y2 or x4 <= x1 or y4 <= y1 or x3 >= x2:
    area1 = 0
else:
    ty1 = min(y2, y4)
    ty2 = max(y1, y3)
    tx1 = min(x4, x2)
    tx2 = max(x1, x3)
    # print(tx1, ty1, tx2, ty2)
    area1 = (ty1 - ty2) * (tx1 - tx2)

#for 2nd sheet
if y5 >= y2 or x6 <= x1 or x5 >= x2 or y6 <= y1:
    area2 = 0
else:
    ty1 = min(y2, y6)
    ty2 = max(y1, y5)
    tx1 = min(x2, x6)
    tx2 = max(x1, x5)
    # print(tx1, ty1, tx2, ty2)
    area2 = (ty1 - ty2) * (tx1 - tx2)

area = (y2 - y1) * (x2 - x1)
# print(area, area1, area2)
if area - area1 - area2 > 0:
    print('YES')
else:
    if area - area2 - area1 == 0:
        if (x4 < x1 and x1 < x5) or (x2 < x5 and x2 > x4) or (y2 < y3 and y2 > y6) or (y1 > y6 and y1 < y3 ) or (x4 > x1 and x1 < x5) or (x2 > x5 and x2 > x4) or (y2 > y3 and y2 > y6) or (y1 < y6 and y1 < y3 ) or (x4 < x1 and x1 > x5) or (x2 < x5 and x2 < x4) or (y2 < y3 and y2 < y6) or (y1 > y6 and y1 > y3 ) or (x4 > x1 and x1 < x5) or (x2 > x5 and x2 > x4) or (y2 > y3 and y2 > y6) or (y1 < y6 and y1 < y3 ):
            print('YES')
    else:
        print('NO')