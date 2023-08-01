N, K = map(int, input().split())
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
arr = [[0, 0]]
for _ in range(N):
    arr.append(list(map(int, input().split())))


for i in range(1, N + 1):
    for j in range(1, K + 1):
        W = arr[i][0]
        V = arr[i][1]

        if j < W:
            knapsack[i][j] = knapsack[i- 1][j]
        else:
            knapsack[i][j] = max(knapsack[i- 1][j], knapsack[i - 1][j - W] + V)

print(knapsack[N][K])