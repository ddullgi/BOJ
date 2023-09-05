from collections import deque

def check_top(maze):
    for i in range(8):
        for j in range(8):
            if maze[i][j] == "#":
                return i

    return -1

def move_wall(top):
    global maze

    for i in range(6, top - 1, -1):
        for j in range(8):
            maze[i + 1][j] = maze[i][j]

    maze[top] = [".", ".", ".", ".", ".", ".", ".", "."]

def bfs(maze, s, top):
    dxy = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0))
    Q = deque()
    Q.append((s[0], s[1], top))

    while Q:
        t = Q[0][2]

        arr = []
        while Q and Q[0][2] == t:
            temp_y, temp_x, temp_top = Q.popleft()
            if temp_y < top:
                return 1
            arr.append((temp_y, temp_x, temp_top))

        same_top = []

        for y, x, top in arr:
            for dy, dx in dxy:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < 8 and 0 <= nx < 8 and maze[ny][nx] == ".":
                    same_top.append((ny, nx))

        move_wall(top)
        top += 1

        for i, j in same_top:
            if maze[i][j] == ".":
                Q.append((i, j, top))

    return 0

maze = [list(input()) for _ in range(8)]

start = (7, 0)
top = check_top(maze)

print(bfs(maze, start, top))
