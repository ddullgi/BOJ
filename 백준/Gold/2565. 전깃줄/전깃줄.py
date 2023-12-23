n = int(input())
arr = []
dp = [1] * n

for i in range(n):
    a, b = map(int, input().split())
    arr.append([a, b])

arr.sort()

for i in range(1, n):
    for j in range(0, i):
        if arr[j][1] < arr[i][1]:
            dp[i] = max(dp[i], dp[j]+1)     

print(n - max(dp))