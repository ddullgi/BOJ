def func(n, cnt):
    if len(n) > 1:
        num = 0
        for i in str(n):
            num += int(i)
        cnt += 1
        func(str(num), cnt)
    else:
        if int(n) % 3:
            print(cnt)
            print('NO')
        else:
            print(cnt)
            print('YES')

T = str(input())
a = 0
func(T, a)