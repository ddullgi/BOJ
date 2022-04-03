from collections import deque

T = int(input())
info = [[] for _ in range(T+1)]

while True:
    N, M = map(int, input().split())
    if N == -1 and M == -1:
        break
    info[N].append(M)
    info[M].append(N)
score = 0xfffffff
num = 0
k = []
if T == 1:
    k = [1]
    score = 1
    num = 1
for i in range(1, T+1):
    cnt = 1
    visit = [0] * (T+1)
    visit[i] = 1
    Q = deque()
    Q.append(i)
    while Q:
        n = Q.popleft()
        for j in info[n]:
            if visit[j] == 0:
                Q.append(j)
                visit[j] = visit[n] + 1
                if visit[j] > cnt:
                    cnt = visit[j]
    if cnt < score:
        score = cnt
        num = 1
        k = [i]
    elif cnt == score:
        num += 1
        k.append(i)
print(score-1, num)
print(*k)