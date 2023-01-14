def DFS(i, j):
    D = arr[i][j]
    if D != "o":
        arr[i][j] = "o"
        if D == "-":
            if j - 1 >= 0 and arr[i][j - 1] == "-":
                DFS(i, j - 1)
            if j + 1 < M and arr[i][j + 1] == "-":
                DFS(i, j + 1)
        elif D == "|":
            if i - 1 >= 0 and arr[i - 1][j] == "|":
                DFS(i - 1, j)
            if i + 1 < N and arr[i + 1][j] == "|":
                DFS(i + 1, j)




N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == "o":
            continue
        else:
            result += 1
            DFS(i, j)
print(result)