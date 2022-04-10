from heapq import heappop, heappush

def DI(s):
    D = [0xfffff] * (V + 1)
    P = [i for i in range(V + 1)]
    visit = [False] * (V + 1)
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


    for i in D[1:]:
        if i == 0xfffff:
            print('INF')
        else:
            print(i)


V, E = map(int, input().split())
S = int(input())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

DI(S)
