from heapq import heappop, heappush

def DIJKSTRA_PRIORITYQ(s):
    global D, P
    visit = [False] * (V + 1)
    D[s] = 0
    Q = [[0, s]]

    while Q:
        d, u = heappop(Q)
        if visit[u]: continue

        visit[u] = True
        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u
                heappush(Q, [D[v], v])





V = int(input())
E = int(input())
G = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

start, end = map(int, input().split())

D = [0xfffffff] * (V + 1)
P = [i for i in range(V + 1)]
DIJKSTRA_PRIORITYQ(start)
print(D[end])