from collections import deque

def bfs(m, r, c):
    dydx = ((1, 0), (0, 1), (-1, 0), (0, -1))
    Q = deque()
    Q.append((r, c, 0))
    visit = [[0] * 5 for _ in range(5)]
    while Q:
        y, x, d = Q.popleft()
        visit[y][x] = 1
        for dy, dx in dydx:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < 5 and 0 <= nx < 5 and m[ny][nx] != "X" and visit[ny][nx] == 0:
                if m[ny][nx] == "P" and d < 2:
                    return False
                elif m[ny][nx] == "O":
                    Q.append((ny, nx, d + 1))
    return True

def solution(places):
    answer = []
    arr = [(i, j) for i in range(5) for j in range(5)]
    for place in places:
        check = 1
        for i, j in arr:
            if place[i][j] == "P" and bfs(place, i, j) == 0:
                print(i, j, place)
                check = 0
                break
        answer.append(check)
                    
    return answer