T = str(input())
N = str(input())
i = 0
a = len(N)
b = len(T) +2
k = a
cnt = 0
while k <= b:
    if N == T[i:k]:
        i += a
        k += a
        cnt += 1
    else:
        i += 1
        k += 1

print(cnt)