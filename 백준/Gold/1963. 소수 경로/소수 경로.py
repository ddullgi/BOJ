from collections import deque

dec = [1] * 10001

for i in range(2, 101):
    if dec[i]:
        for j in range(i * i, 10001, i):
            dec[j] = 0

def bfs(s, e):
    visit = dec[:]
    Q = deque()
    Q.append((s, 0))
    visit[s] = 2

    while Q:
        password, n = Q.popleft()
        p = str(password)
        if password == e:
            print(n)
            return
        for i in range(4):
            for j in range(10):
                change = int(p[:i] + str(j) + p[i + 1:])
                if visit[change] == 1 and change > 1000:
                    visit[change] = 2
                    Q.append((change, n + 1))

for _ in range(int(input())):
    s, e = map(int, input().split())

    bfs(s, e)