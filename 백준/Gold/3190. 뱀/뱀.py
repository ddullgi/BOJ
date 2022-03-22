from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(input())
K = int(input())
apple = [[0]*(N+1) for _ in range(N+1)]
for _ in range(K):
    y, x = map(int, input().split())
    apple[y][x] = 1
L = int(input())
D = []
for _ in range(L):
    D.append(tuple(map(str, input().split())))

T = 0
Q = deque([(1, 1)])
direction = 1
while True:

    ny = Q[-1][0] + dy[direction]
    nx = Q[-1][1] + dx[direction]
    if ny <= 0 or ny > N or nx <= 0 or nx > N:
        T += 1
        break
    if (ny, nx) in Q:
        T += 1
        break
    else:
        Q.append((ny, nx))
    if apple[ny][nx] == 0:
        Q.popleft()
    else:
        apple[ny][nx] = 0
    T += 1
    for t in D:
        if t[0] == str(T):
            if t[1] == 'D':
                direction = (direction+1) % 4
            else:
                direction = (direction+3) % 4
print(T)