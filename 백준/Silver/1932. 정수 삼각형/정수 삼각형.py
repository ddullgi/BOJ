N = int(input())
Tri = [list(map(int, input().split())) for _ in range(N)]
DP = [[0] * i for i in range(1, N+1)]

for k in range(N):
    DP[N-1][k] = Tri[N-1][k]

for i in range(N-2, -1, -1):
    for j in range(i+1):
        DP[i][j] = max(DP[i+1][j], DP[i+1][j+1]) + Tri[i][j]
        
print(DP[0][0])