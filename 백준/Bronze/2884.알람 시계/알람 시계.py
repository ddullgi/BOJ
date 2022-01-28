h, m = map(int, input().split())
hh = 0
mm = 0

if m >= 45:
    mm = m - 45
    hh = h
else:
    mm = m + 15
    if h == 0:
        hh = 23
    else:
        hh = h - 1

print(hh, mm)