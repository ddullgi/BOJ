from collections import deque

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
visit = [[[0]*2 for _ in range(M)] for _ in range(N)]
visit[0][0][1] = 1
dyx = ((1, 0), (-1, 0), (0, 1), (0, -1))
Q = deque()
Q.append((0, 0, 1))
while Q:
    y, x, w = Q.popleft()
    for dy, dx in dyx:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < N and 0 <= nx < M:
            if arr[ny][nx] == '1' and w == 1 and visit[ny][nx][0] == 0 :
                visit[ny][nx][0] = visit[y][x][1] + 1
                Q.append((ny, nx, 0))
            elif arr[ny][nx] == '0':
                if visit[ny][nx][1] == 0 and w == 1:
                    visit[ny][nx][1] = visit[y][x][1] + 1
                    Q.append((ny, nx, 1))
                elif visit[ny][nx][0] == 0 and w == 0:
                    visit[ny][nx][0] = visit[y][x][0] + 1
                    Q.append((ny, nx, 0))
if min(visit[N-1][M-1]) == 0:
    result = max(visit[N-1][M-1])
else:
    result = min(visit[N-1][M-1])
if result == 0:
    print(-1)
else:
    print(result)