x, y = map(str, input().split())
a = b = ''
for i in range(3):
    a = x[i] + a
    b = y[i] + b

if int(a) > int(b):
    print(int(a))
else:
    print(int(b))