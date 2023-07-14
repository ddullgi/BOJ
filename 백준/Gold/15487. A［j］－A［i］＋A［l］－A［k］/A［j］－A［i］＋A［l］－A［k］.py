N = int(input())
arr = list(map(int, input().split()))
fdp = [(arr[1] - arr[0], min(arr[0], arr[1]))]
bdp = [False] * (N - 3)
bdp[-1] = (arr[-1] - arr[-2], max(arr[-2], arr[-1]))

for i in range(2, N - 2):
    fdp.append((max(fdp[-1][0], arr[i] - fdp[-1][1]), min(fdp[-1][1], arr[i])))

for j in range(N - 5, -1, -1):
    bdp[j] = (max(bdp[j + 1][0], bdp[j + 1][1] - arr[j + 2]), max(arr[j + 2], bdp[j + 1][1]))

answer = -0xffffffffff

for k in range(N - 3):
    answer = max(answer, fdp[k][0] + bdp[k][0])

print(answer)