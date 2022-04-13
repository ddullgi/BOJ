N = int(input())
RGB = []
RGB = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * 3 for _ in range(N+1)]
for j in range(1, N + 1):
    for m in range(3):
        minV = 0xfffff
        for k in range(3):
            if k == m:
                continue
            minV = min(minV, DP[j-1][k])
        DP[j][m] = minV + RGB[j-1][m]

print(min(DP[N]))