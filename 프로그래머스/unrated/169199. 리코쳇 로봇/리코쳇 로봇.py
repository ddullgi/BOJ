from collections import deque

def solution(board):
    answer = 0
    INF = 0xfffffffffff
    Q = deque()
    N = len(board)
    M = len(board[0])
    start, end = [0, 0], [0, 0]
    visit = [[INF] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == "R":
                start = [i, j]
            elif board[i][j] == "G":
                end = [i, j]
    dyx = ((0, 1), (1, 0), (0, -1), (-1, 0))
    visit[start[0]][start[1]] = 0
    Q.append((start[0], start[1], 0))
    
    while Q:
        if visit[end[0]][end[1]] != INF:
            return visit[end[0]][end[1]]
        
        
        y, x, d = Q.popleft()
        for dy, dx in dyx:
            ny, nx, nd = y, x, d + 1
            while 0 <= ny + dy < N and 0 <= nx + dx < M and board[ny + dy][nx + dx] != "D":
                ny, nx = ny + dy, nx + dx
                
            
            if nd < visit[ny][nx]:
                visit[ny][nx] = nd
                Q.append((ny, nx, nd))
    
    
    return -1