from collections import deque


def bfs():
    global safe, result
    arr2 = [i[:] for i in arr]
    cnt = safe - 3
    Q = deque()
    for v in virus:
        Q.append(v)
    while Q:
        y, x = Q.popleft()
        for dy, dx in dyx:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < M and arr2[ny][nx] == 0:
                arr2[ny][nx] = 2
                Q.append((ny, nx))
                cnt -= 1
    if cnt > result:
        result = cnt

N, M = map(int, input().split())
lst = []
arr = [list(map(int, input().split())) for _ in range(N)]
# 초기 안전구역 개수
safe = 0

# 바이러스 초기 위치 탐색
virus = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            virus.append((i, j))
        elif arr[i][j] == 0:
            lst.append((i, j))
            safe += 1
# 결과 값
result = 0

dyx = ((1, 0), (-1, 0), (0, 1), (0, -1))



for i in range(safe):
    for j in range(i, safe):
        for k in range(j, safe):
            arr[lst[i][0]][lst[i][1]] = 1
            arr[lst[j][0]][lst[j][1]] = 1
            arr[lst[k][0]][lst[k][1]] = 1
            bfs()
            arr[lst[i][0]][lst[i][1]] = 0
            arr[lst[j][0]][lst[j][1]] = 0
            arr[lst[k][0]][lst[k][1]] = 0


print(result)