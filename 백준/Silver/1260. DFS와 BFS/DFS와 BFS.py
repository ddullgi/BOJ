from collections import deque

def dfs(visit, V):
    visit.append(V)

    for i in directions[V]:
        if i not in visit:
            dfs(visit, i)
    return visit

def bfs():
    visit = []
    Q = deque()
    Q.append(V)
    visit.append(V)
    while Q:
        s = Q.popleft()
        for i in directions[s]:
            if i not in visit:
                visit.append(i)
                Q.append(i)
    return visit




N, M, V = map(int, input().split())
directions = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    directions[a].append(b)
    directions[b].append(a)
    directions[a].sort()
    directions[b].sort()
print(" ".join(str(i) for i in dfs([], V)))
print(" ".join(str(i) for i in bfs()))