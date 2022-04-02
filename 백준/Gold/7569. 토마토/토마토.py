from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for i in range(H)]
Q = deque()
for i in range(N):
    for j in range(M):
        for k in range(H):
            if arr[k][i][j] == 1:
                Q.append((i, j, k, 0))

dyx = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

result = 0
while Q:
    ry, rx, rz, cnt = Q.popleft()
    if cnt > result:
        result = cnt
    for dy, dx, dz in dyx:
        ny = ry + dy
        nx = rx + dx
        nz = rz + dz
        if 0 <= ny < N and 0 <= nx < M and 0 <= nz < H and arr[nz][ny][nx] == 0:
            Q.append((ny, nx, nz, cnt + 1))
            arr[nz][ny][nx] = 1

def check(m, n, h):
    global result
    for i in range(n):
        for j in range(m):
            for k in range(h):
                if arr[k][i][j] == 0:
                    result = -1
                    return
check(M, N, H)
print(result)