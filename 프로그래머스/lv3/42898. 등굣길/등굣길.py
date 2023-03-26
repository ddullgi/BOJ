def solution(m, n, puddles):
    
    maze = [[-1 for _ in range(m)] for _ in range(n)]
    maze[0][0] = 1
    for x, y in puddles:
        maze[y - 1][x - 1] = 0
    
    
    for y in range(n):
        for x in range(m):
            if maze[y][x] == -1:
                if y == 0:
                    maze[y][x] = maze[y][x - 1]
                elif x == 0:
                    maze[y][x] = maze[y - 1][x]
                else:
                    maze[y][x] = maze[y][x - 1] + maze[y - 1][x]
    
    answer = maze[n - 1][m - 1] % 1000000007

    
    
    return answer