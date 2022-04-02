from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
Q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            Q.append((i, j, 0))

dyx = ((1, 0), (-1, 0), (0, 1), (0, -1))

result = 0
while Q:
    ry, rx, cnt = Q.popleft()
    if cnt > result:
        result = cnt
    for dy, dx in dyx:
        ny = ry + dy
        nx = rx + dx
        if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 0:
            Q.append((ny, nx, cnt + 1))
            arr[ny][nx] = 1

def check(m, n):
    global result
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                result = -1
                return
check(M, N)
print(result)