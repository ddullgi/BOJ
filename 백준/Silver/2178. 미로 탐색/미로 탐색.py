from collections import deque

dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
Q = deque()
Q.append((0, 0))
visit[0][0] = 1
while Q:
    y, x = Q.popleft()
    for dy, dx in dxy:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < N and 0 <= nx < M and visit[ny][nx] == 0 and arr[ny][nx] == '1':
            visit[ny][nx] = visit[y][x] + 1
            Q.append((ny, nx))

print(visit[N-1][M-1])