from collections import deque
import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b =  map(int, input().split())  
    graph[a].append(b)

dis = [-1] * (N + 1)
dis[X] = 0

Q = deque([X])
while Q:
    now = Q.popleft()

    for next in graph[now]:
        if dis[next] == -1:
            dis[next] = dis[now] + 1
            Q.append(next)

if K in dis:
    for i in range(1, N+1):
        if dis[i] == K:
            print(i)
            check = True
else:
    print(-1)