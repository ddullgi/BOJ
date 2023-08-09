import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

ps = [0] * (2 * N + 1)
for i in range(2 * N):
    ps[i + 1] = ps[i] + arr[i % N]

result = 0
total = sum(arr)
r = 1

for l in range(2 * N):
        while r < 2 * N + 1 and ps[r] - ps[l] <= total - ps[r] + ps[l]:
            result = max(result, ps[r] - ps[l])
            r += 1

print(result)