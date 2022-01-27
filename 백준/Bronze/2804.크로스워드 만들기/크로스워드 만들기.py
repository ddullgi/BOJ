A, B = map(str, input().split())
p = 0
for i in range(0,len(A)):
    if A[i] in B:
        p = i
        break
check = 0
for j in range(len(B)):
    back_dot = len(A)-p-1
    if B[j] == A[p]:
        if check == 0:
            print(A)
            check = 1
        else:
            print('.'* p + B[j] + '.' * back_dot)
    else:
        print('.'* p + B[j] + '.' * back_dot)
