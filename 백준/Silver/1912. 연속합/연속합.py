N = int(input())
arr = list(map(int, input().split()))
memo = [None] * N
memo[0] = arr[0]
for i in range(1, N):
    if memo[i - 1] < 0 and arr[i] < 0:
        memo[i] = max(memo[i - 1], arr[i])
    elif memo[i - 1] < 0:
        memo[i] = arr[i]
    else:
        memo[i] = memo[i - 1] + arr[i]
print(max(memo))