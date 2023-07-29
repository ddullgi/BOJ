from collections import deque
from copy import deepcopy

horse = ((1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2))
dxdxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

K = int(input())
W, H = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(H)]
maze = [deepcopy(maze) for _ in range(K + 1)]

Q = deque()
Q.append((0, 0, K, 0))
result = -1

while Q:
    x, y, k, d = Q.popleft()
    if (x, y) == (W - 1, H - 1):
        result = d
        break

    for dx, dy in dxdxy:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < W and 0 <= ny < H and maze[k - 1][ny][nx] == 0:
            maze[k - 1][ny][nx] = 2
            Q.append((nx, ny, k, d + 1))

    if k:
        for dx, dy in horse:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < W and 0 <= ny < H and maze[k - 2][ny][nx] == 0:
                maze[k - 2][ny][nx] = 2
                Q.append((nx, ny, k - 1, d + 1))

print(result)