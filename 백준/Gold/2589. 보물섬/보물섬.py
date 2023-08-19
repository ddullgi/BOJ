from collections import deque

N, M = map(int, input().split())
maze = [list(input()) for _ in range(N)]

dydx = ((1, 0), (0, 1), (-1, 0), (0, -1))

def bfs(i,j):
  queue=deque()
  queue.append((i,j))
  visited=[[0] * M for _ in range(N)]
  visited[i][j] = 1
  cnt = 0
  while queue:
    y, x =queue.popleft()
    for dy, dx in dydx:
      nx = x + dx
      ny = y + dy
      if 0 <= nx < M and 0 <= ny < N and maze[ny][nx] == 'L' and visited[ny][nx] == 0:
        visited[ny][nx] = visited[y][x] + 1
        cnt = max(cnt, visited[ny][nx])
        queue.append((ny, nx))
  return cnt - 1

result = 0
for i in range(N):
  for j in range(M):
    if maze[i][j] == 'L':
      result = max(result, bfs(i, j))

print(result)