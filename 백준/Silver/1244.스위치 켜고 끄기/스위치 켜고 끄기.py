def female(list_n, a, b):
    if a > 0 and b < len(list_n) - 1:
        if list_n[a-1] == list_n[b+1]:
            return female(list_n, a-1, b+1)
        else:
            return [a,b]
    else:
        return [a,b]

T = int(input())
x = list(map(int, input().split()))
N = int(input())

for i in range(N):
    sex, num = map(int, input().split())
    
    if sex == 1:
        for n in range(len(x)):
            if (n + 1)% num == 0:
                if x[n] == 0:
                    x[n] = 1
                else:
                    x[n] = 0
    else:
        dot = female(x, num-1, num-1)
        for j in range(dot[0],dot[1]+1):
            if x[j] == 0:
                x[j] = 1
            else:
                x[j] = 0

for h in range(len(x)):
    if h == 0:
        print(x[h], end=' ')
    elif h%20 == 0:
        print()
        print(x[h], end=' ')
    else:
        print(x[h], end=' ')