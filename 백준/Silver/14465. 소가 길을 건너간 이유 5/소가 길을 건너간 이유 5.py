N, K, B = map(int, input().split())
arr = [1] * (N + 1)
for _ in range(B):
    arr[int(input())] = 0

window = sum(arr[1:K + 1])
m = K - window
for i in range(2, N-K+2):
    window = window - arr[i - 1] + arr[i - 1 + K]
    m = min(m, K - window)
    if m == 0:
        break

print(m)