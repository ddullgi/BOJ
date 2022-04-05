V, E = map(int, input().split())
edges = []
for _ in range(E):
    edges.append(tuple(map(int, input().split())))

edges.sort(key=lambda x: x[2])

p = [i for i in range(V + 1)]


def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

cnt = ans = 0
mst = []
for edge in edges:
    u, v, w = edge
    a = find_set(u)
    b = find_set(v)
    if a == b:
        continue
    mst.append(edge)
    ans += w
    p[a] = b
    cnt += 1
    if cnt == V:
        break
print(ans)