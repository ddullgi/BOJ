from collections import deque

def find_s(maps, n, m):
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                return i, j

def bfs(y, x, goal, n, m, dd, maps):
    dxy = ((-1, 0), (0, -1), (1, 0), (0, 1))
    
    if dd == -1:
        return -1, -1, -1
    
    visit = [[0] * m for _ in range(n)]
    visit[y][x] = dd
    Q = deque()
    Q.append((y, x, dd))
    
    while Q:
        y, x, d = Q.popleft()
        if maps[y][x] == goal:
            return y, x, d
        for dy, dx in dxy:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] != "X" and visit[ny][nx] == 0:
                visit[ny][nx] = d + 1
                Q.append((ny, nx, d + 1))
    
    return -1, -1, -1

def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    y, x = find_s(maps, n, m)
    ny, nx, d = bfs(y, x, "L", n, m, 0, maps)
    gy, gx, answer = bfs(ny, nx, "E", n, m, d, maps)
    return answer