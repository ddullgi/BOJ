H, W = map(int, input().split())

e = abs(H - W) + 1

arr = [[0] * e for _ in range(e)]
for i in range(e):
    arr[0][i] = 1

for i in range(1, e):
    for j in range(i, e):
        arr[i][j] = arr[i - 1][j] + arr[i][j - 1]

answer = arr[-1][-1]
print(answer)