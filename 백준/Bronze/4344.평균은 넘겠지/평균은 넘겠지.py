T = int(input())
for i in range(T):
    cnt = 0
    A = list(map(int, input().split()))
    result = sum(A[1:])/A[0]
    for j in A[1:]:
        if j > result:
            cnt += 1
    B = cnt / A[0] * 100
    print(f'{B:.3f}%')