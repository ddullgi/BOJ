N = int(input())
arr = [1] * 40001
arr[0] = arr[1] = 0
arr2 = []

for i in range(2, 201):
    if arr[i]:
        for j in range(i * i, 40001, i):
            arr[j] = 0

for i in range(2, 40001):
    if arr[i]:
        arr2.append(i)

dp = [1] + [0] * N

for i in arr2:
    for j in range(i, N + 1):
        dp[j] += dp[j-i]
        dp[j] = dp[j] % 123456789
print(dp[N])