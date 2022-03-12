N = int(input())
arr = [0]
stack = [0] * (N+1)
money = 0
maxM = 0
for _ in range(N):
    arr.append(tuple(map(int, input().split())))

for i in range(N, 0, -1):
    if (i + arr[i][0] - 1) > N:
        stack[i] = maxM
        continue
    elif (i + arr[i][0] - 1) == N:
        money = arr[i][1]
    else:
        money = arr[i][1] + stack[i + arr[i][0]]
    if money > maxM:
        maxM = money
    stack[i] = maxM

print(maxM)