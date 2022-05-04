from heapq import heappop, heappush

def DI(s):
    D = [0xffffffff] * (N + 1)
    P = [i for i in range(N + 1)]
    visit = [False] * (N + 1)
    D[s] = 0
    Q = [[0, s]]
    while Q:
        d, u = heappop(Q)
        if visit[u]:
            continue

        visit[u] = True
        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u
                heappush(Q, [D[v], v])
    print(D[N])



N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((B, C))
    G[B].append((A, C))


DI(1)