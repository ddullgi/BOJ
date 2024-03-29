from heapq import heappop, heappush

def find_root(start, end):
    D = [0xffffff] * (N + 1)

    visit = [False] * (N + 1)
    Q = [(0, start)]
    D[start] = 0
    while Q:
        d, u = heappop(Q)
        if visit[u]:
            continue

        visit[u] = True
        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                heappush(Q,(D[v], v))
    return D


N, E = map(int, input().split())
G = [[] for _ in range(N + 1)]

if E == 0:
    result = -1
else:
    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u].append((v, w))
        G[v].append((u, w))

v1, v2 = map(int, input().split())
XXX = find_root(1, v1)
XXX2 = find_root(N, v1)
v1v2 = find_root(v1, v2)[v2]

result1 = XXX[v1] + v1v2 + XXX2[v2]
result2 = XXX[v2] + v1v2 + XXX2[v1]

result = min(result1, result2)
if result >= 0xffffff:
    result = -1
print(result)