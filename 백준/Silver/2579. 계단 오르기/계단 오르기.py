T = int(input())
arr = [0]
for _ in range(T):
    arr += [int(input())]
memo = [-1] * 301
memo[0] = 0
memo[1] = arr[1]
if T > 1:
    memo[2] = arr[1] + arr[2]

def step(x):
    if memo[x] != -1:
        return memo[x]
    else:
        if step(x-2) > arr[x-1] + step(x-3):
            memo[x] = step(x-2) + arr[x]
        else:
            memo[x] = arr[x-1] + step(x-3) + arr[x]
        return memo[x]

print(step(T))