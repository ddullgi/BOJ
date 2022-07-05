import sys
from collections import deque
input = sys.stdin.readline
for tc in range(int(input())):
    M, N, K = map(int, input().split())

    arr = [[0] * M for _ in range(N)]
    for _ in range(K):
        y, x = map(int, input().split())
        arr[x][y] = 1

    dydyx = ((1, 0), (-1, 0), (0, 1), (0, -1))

    result = 0

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                continue
            Q = deque()
            Q.append((i, j))
            cnt = 1
            arr[i][j] = 0

            while Q:
                y, x = Q.popleft()
                for dy, dx in dydyx:
                    ny = y+dy
                    nx = x+dx
                    if 0 <= ny < N and 0 <= nx < M and arr[ny][nx] == 1:
                        Q.append((ny, nx))
                        arr[ny][nx] = 0

            result += 1

    print(result)