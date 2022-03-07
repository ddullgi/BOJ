arr = [-1] * 42
arr[0] = 0
arr[1] = 1
arr[41] = 1
def fibo(x):
    if arr[x] != -1:
        return arr[x]
    else:
        arr[x] = fibo(x-1) + fibo(x-2)
        return arr[x]

T = int(input())
for _ in range(T):
    N = int(input())
    print(fibo(N-1), fibo(N))