T = str(input())
T = T.upper()
A = []
A.extend(T)
k = set(A)
max = 0
check = 0
alpha = ''
for i in k:
    n = 0
    for j in A:
        if i == j:
            n += 1
    if n > max:
        max = n
        alpha = i
    elif n == max:
        check = n
if max == check:
    print('?')
else:
    print(alpha)