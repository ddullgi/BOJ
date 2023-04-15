from collections import deque

def solution(maps):
    dxdy = ((1, 0), (0, 1), (-1, 0), (0, -1))
    N = len(maps)
    M = len(maps[0])
    answer = -1
    
    Q = deque()
    Q.append((0, 0, 1))
    maps[0][0] = -1
    
    while Q:
        x, y, d = Q.popleft()
        if x == M - 1 and y == N - 1:
            answer = d
            break
        for dx, dy in dxdy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < M and 0 <= ny < N and maps[ny][nx] == 1:
                maps[ny][nx] = -1
                Q.append((nx, ny, d + 1))
        
    return answer