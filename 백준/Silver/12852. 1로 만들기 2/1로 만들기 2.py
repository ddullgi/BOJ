N = int(input())
dp = [0] * (N + 1) 
arr = ["" for _ in range(N + 1)] 
arr[1] = "1"

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    p = i - 1
    if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
        dp[i] = dp[i // 3] + 1
        p = i // 3
    if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
        dp[i] = dp[i // 2] + 1
        p = i // 2
    arr[i] = str(i) + " " + arr[p]

print(dp[N])
print(arr[N])
