from collections import deque

def bfs():
    Q = deque()
    Q.append([home[0], home[1]])
    while Q:
        x, y = Q.popleft()
        if abs(x - fest[0]) + abs(y - fest[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            if not visited[i]:
                new_x, new_y = conv[i]
                if abs(x - new_x) + abs(y - new_y) <= 1000:
                    Q.append([new_x, new_y])
                    visited[i] = 1
    print("sad")
    return

t = int(input())
for i in range(t):
    n = int(input())
    home = [int(x) for x in input().split()]
    conv = []
    for j in range(n):
        x, y = map(int, input().split())
        conv.append([x, y])
    fest = [int(x) for x in input().split()]
    visited = [0 for i in range(n + 1)]
    bfs()