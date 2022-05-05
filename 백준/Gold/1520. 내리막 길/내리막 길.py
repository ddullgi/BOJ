from collections import deque

M, N = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(M)]
DP = [[0] * N for _ in range(M)]
DP_dir = [[[0, 0, 0, 0] for _ in range(N)] for _ in range(M)]

DP[0][0] = 1
Q = deque()
Q.append((0, 0))

while Q:
    y, x = Q.popleft()
    for dy, dx, d in ((0, 1, 0), (1, 0, 1), (-1, 0, 2), (0, -1, 3)):
        ny = y + dy
        nx = x + dx
        # 범위 체크
        if 0 <= ny < M and 0 <= nx < N and area[y][x] > area[ny][nx]:
            if DP_dir[ny][nx][d] == 0:
                DP[ny][nx] += DP[y][x]
                DP_dir[ny][nx][d] += DP[y][x]
                Q.append((ny, nx))
            elif DP_dir[ny][nx][d] < DP[y][x]:
                DP_dir[ny][nx][d] = DP[y][x]
                DP[ny][nx] = sum(DP_dir[ny][nx])
                Q.append((ny, nx))


print(DP[M-1][N-1])