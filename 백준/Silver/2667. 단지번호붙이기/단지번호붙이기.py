from collections import deque

T = int(input())
arr = [list(map(int, input())) for _ in range(T)]

dydyx = ((1, 0), (-1, 0), (0, 1), (0, -1))

result = []

for i in range(T):
    for j in range(T):
        if arr[i][j] == 0:
            continue
        Q = deque()
        Q.append((i, j))
        cnt = 1
        arr[i][j] = 0

        while Q:
            y, x = Q.popleft()
            for dy, dx in dydyx:
                ny = y+dy
                nx = x+dx
                if 0 <= ny < T and 0 <= nx < T and arr[ny][nx] == 1:
                    Q.append((ny, nx))
                    arr[ny][nx] = 0
                    cnt += 1
        result.append(cnt)
result.sort()
print(len(result))
for i in result:
    print(i)