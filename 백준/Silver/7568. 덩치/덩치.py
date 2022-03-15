N = int(input())
arr = []
for _ in range(N):
    arr += [list(map(int, input().split())) + [0]]
for i in range(N):
    for j in range(N):
        if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
            arr[i][2] += 1
    print(arr[i][2]+1, end=' ')