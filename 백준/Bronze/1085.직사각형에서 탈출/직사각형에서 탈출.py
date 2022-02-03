x, y, w, h = map(int, input().split())
if w/2 > x:
    d_1 = x
else:
    d_1 = w - x
if h/2 > y:
    d_2 = y
else:
    d_2 = h -y
if d_1 < d_2:
    print(d_1)
else:
    print(d_2)