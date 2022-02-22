V = int(input())
E = int(input())

graph = [[] for _ in range(100)]

for _ in range(E):
    n, m = map(int, input().split())
    graph[n-1] += [m]
    graph[m-1] += [n]
stack = [1, ]
visited = []
while stack:
    node = stack.pop()
    if node not in visited:
        visited.append(node)
        stack.extend(graph[node-1])
print(len(visited)-1)