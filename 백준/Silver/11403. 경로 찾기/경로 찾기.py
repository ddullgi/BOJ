N = int(input())
maze = []

for _ in range(N):
    maze.append(list(map(int,input().split())))

for k in range(N):
    for i in range(N):
        for j in range(N):
            if maze[i][k] and maze[k][j]:
                maze[i][j]=1

for r in maze:
    for c in r:
        print(c, end = " ")
    print()