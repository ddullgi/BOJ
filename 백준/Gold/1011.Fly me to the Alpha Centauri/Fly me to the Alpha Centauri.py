T = int(input())
for i in range(T):
    x, y = map(int, input().split())
    d = y - x
    cnt = 0
    n = 0
    while True:
        n += 1
        if d - n ** 2 <= 0:
            break
        elif d - n ** 2 - n<= 0:
            break

    
    if d - n ** 2 <= 0:
        cnt = 2 * n - 1
    else:
        cnt = 2 * n
    print(cnt)