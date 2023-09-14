def dfs(depth):
    global count
    if depth == N * M:
        count += 1
        return

    r = depth // M + 1
    c = depth % M + 1

    if arr[r - 1][c] == 0 or arr[r][c - 1] == 0 or arr[r - 1][c - 1] == 0:
        arr[r][c] = 1
        dfs(depth + 1)
        arr[r][c] = 0
    dfs(depth + 1)

N, M = map(int, input().split())
arr = [[0] * (M + 1) for _ in range(N + 1)]
count = 0

dfs(0)
print(count)