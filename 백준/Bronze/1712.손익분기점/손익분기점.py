a, b, c = map(int, input().split())
m = -1
d = c - b
cnt = 0
if d <= 0:
    cnt = -1
else:
    cnt = a // d + 1

print(cnt)