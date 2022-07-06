from collections import deque

N = int(input())
a, b = map(int, input().split())
n = int(input())

tree = [[]for i in range(N + 1)]
visit = [0] * (N + 1)



for _ in range(n):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

Q = deque()
Q.append((a, 0))
result = -1
while Q:
    r, s = Q.popleft()
    if r == b:
        result = s
        break
    for j in tree[r]:
        if visit[j] == 1:
            continue
        visit[j] = 1
        Q.append((j, s + 1))

print(result)