arr = [0] * 101
arr[0:6] = 0, 1, 1, 1, 2, 2

T = int(input())
for _ in range(T):
    N = int(input())
    if N > 5:
        for i in range(6, N+1):
            arr[i] = arr[i - 5] + arr[i - 1]
    print(arr[N])