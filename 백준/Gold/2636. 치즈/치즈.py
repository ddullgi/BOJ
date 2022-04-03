from collections import deque

def airCheck(i, j, n):
    global cheese
    if arr[i][j] == 0:
        air = deque()
        air.append((i, j))
        while air:
            y, x = air.popleft()
            for dy, dx in dyx:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < N and 0 <= nx < M:
                    if arr[ny][nx] == 0:
                        air.append((ny, nx))
                        arr[ny][nx] = -1
                    elif arr[ny][nx] == 1:
                        cheese.append((ny, nx))
                        arr[ny][nx] = n

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dyx = ((1, 0), (-1, 0), (0, 1), (0, -1))

num = 2
cheese = deque()
airCheck(0, 0, num)

if cheese:
    cnt = 2
else:
    cnt = 1
while cheese:
    y, x = cheese.popleft()
    for dy, dx in dyx:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < N and 0 <= nx < M:
            num = arr[y][x] + 1
            if arr[ny][nx] == 1:
                cheese.append((ny, nx))
                arr[ny][nx] = num
                if num > cnt:
                    cnt = num
            if arr[ny][nx] == 0:
                airCheck(ny, nx, num)
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == cnt:
            result += 1
print(cnt-1)
print(result)