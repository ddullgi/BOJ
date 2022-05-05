from heapq import heappop, heappush

def find_root(start, end):
    D = [0xffffff] * (N + 1)
    P = [i for i in range(N + 1)]
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
                P[v] = u
                heappush(Q,(D[v], v))
    return D[end]


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

v1v2 = find_root(v1, v2)
# SV1, PV1 = find_root(1, v1)
# SV2, PV2 = find_root(1, v2)

# n1 = v1
# while True:
#     if PV1[n1] == v2:
#         result1 = find_root(1, v1)[0] + find_root(v1, N)[0]
#         break
#     elif PV1[n1] == 1:
#         result1 = find_root(1, v1)[0] + v1v2 + find_root(v2, N)[0]
#         break
#     else:
#         n1 = PV1[n1]
#
# n2 = v2
# while True:
#     if PV2[n2] == v1:
#         result2 = find_root(1, v2)[0] + find_root(v2, N)[0]
#         break
#     elif PV2[n2] == 1:
#         result2 = find_root(1, v2)[0] + v1v2 + find_root(v1, N)[0]
#         break
#     else:
#         n2 = PV2[n2]

result1 = find_root(1, v1) + v1v2 + find_root(v2, N)
result2 = find_root(1, v2) + v1v2 + find_root(v1, N)

result = min(result1, result2)
if result >= 0xffffff:
    result = -1
print(result)
