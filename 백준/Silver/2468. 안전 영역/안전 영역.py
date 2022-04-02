from collections import deque
import copy

N = int(input())
origin = [list(map(int, input().split())) for _ in range(N)]

maxh = 0
for i in range(N):
    for j in range(N):
        if origin[i][j] > maxh:
            maxh = origin[i][j]

dyx = ((1, 0), (-1, 0), (0, 1), (0, -1))
result = 0
for k in range(maxh):
    arr = copy.deepcopy(origin)
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] <= k:
                arr[i][j] = 0
            else:
                Q = deque()
                Q.append((i, j))
                while Q:
                    y, x = Q.popleft()
                    arr[y][x] = 0
                    for dy, dx in dyx:
                        ny = y + dy
                        nx = x + dx
                        if 0 <= ny < N and 0 <= nx < N and arr[ny][nx] > k:
                            Q.append((ny, nx))
                            arr[ny][nx] = 0
                cnt += 1
    if cnt > result:
        result = cnt
print(result)