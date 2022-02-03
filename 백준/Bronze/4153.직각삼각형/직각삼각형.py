while True:
    a = list(map(int, input().split()))
    max = 0
    b = c = 0
    for i in range(3):
        if a[i] > max:
            max = a[i]
            k = i
    if k == 0:
        b = 1
        c = 2
    elif k == 1:
        b = 0
        c = 2
    else:
        b = 0
        c = 1
    if a[0] == 0 and a[1] == 0 and a[2] == 0:
        break
    elif a[b] ** 2 + a[c] ** 2 == a[k] ** 2:
        print('right')
    else:
        print('wrong')