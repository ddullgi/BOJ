import sys
sys.setrecursionlimit(100000)


M, N, K = map(int, input().split())
square = [[0] * M for _ in range(N)]
for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            square[i][j] = -1

dydyx = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(y, x):
    global square, check, cnt
    for dy, dx in dydyx:
        ny, nx = y+dy, x+dx
        if 0 <= ny < N and 0 <= nx < M:
            if square[ny][nx] == 0:
                square[ny][nx] = check
                cnt += 1
                bfs(ny, nx)

            elif square[ny][nx] == -1:
                continue
    return cnt
result = {}
check = 1
for i in range(N):
    for j in range(M):
        if square[i][j] == 0:
            square[i][j] = check
            cnt = 1
            result[check] = bfs(i, j)
            check += 1

area = sorted(result.values())
print(len(area))
print(*area)