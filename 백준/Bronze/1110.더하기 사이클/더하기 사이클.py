cnt = 0
A = str(input())
i = A
while True:
    cnt += 1
    if len(i) < 2:
        i = '0' + i
    K = str(int(i[0]) + int(i[1]))
    if len(K) < 2:
        i = i[1] + K
    else:
        i = i[1] + K[1]
    if i == A:
        break
    elif i == '0' + A:
        break
print(cnt)
