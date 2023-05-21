from collections import deque

def BFS(x, y, n, m, visit, maps):
    Q = deque([(x, y)])
    visit[x][y] = 1
    size = int(maps[x][y])
    dxy = ((-1, 0), (1, 0), (0, 1), (0, -1))
    while Q:
        cx, cy = Q.popleft()

        for dx, dy in dxy:
            nx = cx + dx
            ny = cy + dy

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X':
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    size += int(maps[nx][ny])
                    Q.append((nx, ny))

    return visit, size

def solution(maps):
    answer = []
    n = len(maps)
    m = len(maps[0])
    visit = [[0] * m for _ in range(n)] 
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X" and visit[i][j] == 0:
                visit, ans = BFS(i, j, n, m, visit, maps)
                answer.append(ans)
    if answer:
        return sorted(answer)
    else:
        return [-1]
    