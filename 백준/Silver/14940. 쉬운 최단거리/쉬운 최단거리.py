from collections import deque

dxdy = ((1, 0), (0, 1), (-1, 0), (0, -1))

n, m = map(int, input().split())
Q = deque()
arr = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]
ressult = [[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            check[i][j] = 1
            ressult[i][j] = 0
            Q.append((i, j))
        if arr[i][j] == 0:
            ressult[i][j] = 0


while Q:
    y, x = Q.popleft()
    for dy, dx in dxdy:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < n and 0 <= nx < m and check[ny][nx] == 0 and arr[ny][nx] == 1:
            ressult[ny][nx] = ressult[y][x] + 1
            check[ny][nx] = 1
            Q.append((ny, nx))

for l in ressult:
    print(*l)
