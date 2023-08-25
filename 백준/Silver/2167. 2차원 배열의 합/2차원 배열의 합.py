import sys
input = sys.stdin.readline
N, M = map(int, input().split())
screen = [list(map(int, input().split())) for _ in range(N)]
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]



for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = -prefix_sum[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] + screen[i - 1][j - 1]

K = int(input())

for i in range(K):
    r1, c1, r2, c2 = map(int, input().split())
    ans = prefix_sum[r2][c2] - prefix_sum[r1-1][c2] - prefix_sum[r2][c1-1] + prefix_sum[r1-1][c1-1]
    print(ans)
