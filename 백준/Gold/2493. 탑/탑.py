def check(h, index, n):
    if H[n] < h:
        if result[n] == 0:
            result[index] = 0
        else:
            check(h, index, result[n]-1)
    else:
        result[index] = n+1





N = int(input())
H = list(map(int, input().split()))
result = [0] * N

for i in range(1, N):
    check(H[i], i, i-1)

print(*result)