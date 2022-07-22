import sys
input = sys.stdin.readline
from collections import deque

V, E, R = map(int, input().split())
directions = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    directions[a].append(b)
    directions[b].append(a)

for i in range(1, V+1):
    directions[i].sort(reverse=True)

visit = [0] * (V + 1)
Q = deque()
Q.append(R)
visit[R] = 1
step = 1
while Q:
    s = Q.popleft()
    for i in directions[s]:
        if visit[i] == 0:
            visit[i] = step + 1
            Q.append(i)
            step += 1

for i in range(1, V + 1):
    print(visit[i])