T = list(map(int, input().split()))
check = 0
for i in range(1,len(T)):
    if T[i-1] > T[i]:
        check -= 1
    else:
        check += 1

if check == 7:
    print('ascending')
elif check == -7:
    print('descending')
else:
    print('mixed')