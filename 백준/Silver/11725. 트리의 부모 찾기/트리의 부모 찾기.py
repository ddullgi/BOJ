import sys
from collections import deque
input = sys.stdin.readline


N = int(sys.stdin.readline())
graph = [[] for i in range(N + 1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)

ans = [0]*(N+1)

def bfs():
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if ans[nxt] == 0:
                ans[nxt] = now
                queue.append(nxt)

bfs()
result = ans[2:]
for x in result:
    print(x)