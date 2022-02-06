def x(n):
    if len(str(n)) <=2:
        return True
    else:
        mm = int(str(n)[0]) - int(str(n)[1])
        check = 0
        for i in range(2,len(str(n))):
            if int(str(n)[i-1]) - int(str(n)[i]) == mm:
                check = 0
            else:
                check = 1
        if check == 0:
            return True
        else:
            return False
N = int(input())
cnt = 0
for k in range(1,N+1):
    if x(k) == True:
        cnt += 1

print(cnt)