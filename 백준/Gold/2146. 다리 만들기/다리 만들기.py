from collections import deque

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dyx = ((1, 0), (0, 1), (-1, 0), (0, -1))

Hor = []
n = 1
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            n += 1
            Q = deque()
            Q.append((i, j))
            arr[i][j] = n
            while Q:
                y, x = Q.popleft()
                check = 0
                for dy, dx in dyx:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] == 1:
                        arr[ny][nx] = n
                        Q.append((ny, nx))


for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            for di, dj in dyx:
                ni = i + di
                nj = j + dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                    Hor.append((i, j))
                    break

def BFS(Y, X):
    visit = [[-1] * N for _ in range(N)]
    n = arr[Y][X]
    Q = deque()
    Q.append((Y, X))
    visit[Y][X] = 0
    while Q:
        y, x = Q.popleft()
        for dy, dx in dyx:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == -1:
                if arr[ny][nx] != 0 and arr[ny][nx] != n:
                    return visit[y][x]
                visit[ny][nx] = visit[y][x] + 1
                Q.append((ny, nx))

min_len = 0xffffffff
for a, b in Hor:
    min_len = min(BFS(a, b), min_len)

print(min_len)