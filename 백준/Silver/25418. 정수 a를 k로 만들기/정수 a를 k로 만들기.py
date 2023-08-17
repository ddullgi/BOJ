from collections import deque

Q = deque()
A, K = map(int, input().split())
Q.append((0, A))
visited = {A: 0}

def solution():
    while Q:
        cnt, v = Q.popleft()
        for dv in (v * 2, v + 1):
            if dv == K:
                print(cnt + 1)
                return 
            if dv > K:
                continue
            if dv in visited:
                continue
            visited[dv] = cnt + 1
            Q.append((cnt + 1, dv))

solution()