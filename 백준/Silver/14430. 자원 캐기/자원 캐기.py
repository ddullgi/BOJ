N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * M for _ in range(N)]
dp[0][0] = arr[0][0]
for i in range(N):
    for j in range(M):
        if i == 0 and j == 0:
            continue
        elif i > 0 and j == 0:
            dp[i][j] = dp[i - 1][j]
        elif i == 0 and j > 0:
            dp[i][j] = dp[i][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j -1 ])
        if arr[i][j] == 1:
            dp[i][j] += 1
print(max(map(max, dp)))