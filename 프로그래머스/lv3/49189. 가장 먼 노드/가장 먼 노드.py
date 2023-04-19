from collections import deque

def solution(n, edge):
    edge.sort()
    node = [[] for _ in range(n + 1)]
    visit = [0] * (n + 1)
    for s, e in edge:
        node[s].append(e)
        node[e].append(s)
    
    visit[1] = -1
    Q = deque()
    Q.append((1, 0))
    while Q:
        x, d = Q.popleft()
        for dx in node[x]:
            if visit[dx] == 0:
                visit[dx] = d + 1
                Q.append((dx, d + 1))
    
    M = max(visit)
    answer = visit.count(M)
    return answer