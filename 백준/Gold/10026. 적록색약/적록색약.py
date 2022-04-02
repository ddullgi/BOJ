from collections import deque

def RGB(n):
    cnt = 0
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 1:
                continue
            Q = deque()
            Q.append((i, j))
            while Q:
                y, x = Q.popleft()
                check = arr[y][x]
                for dy, dx in dyx:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < n and 0 <= nx < n and visit[ny][nx] == 0 and arr[ny][nx] == check:
                        Q.append((ny, nx))
                        visit[ny][nx] = 1
            cnt += 1
    return cnt

def RG(n):
    cnt = 0
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visit[i][j] == 1:
                continue
            Q = deque()
            Q.append((i, j))
            while Q:
                y, x = Q.popleft()
                check = arr[y][x]
                for dy, dx in dyx:
                    ny = y + dy
                    nx = x + dx
                    if 0 <= ny < n and 0 <= nx < n and visit[ny][nx] == 0 and arr[ny][nx] == check:
                        Q.append((ny, nx))
                        visit[ny][nx] = 1
            cnt += 1
    return cnt




N = int(input())
arr = [list(str(input())) for _ in range(N)]

dyx = ((1, 0), (-1, 0), (0, 1), (0, -1))

A = RGB(N)
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'R':
            arr[i][j] = 'G'
B = RG(N)
print(A, B)