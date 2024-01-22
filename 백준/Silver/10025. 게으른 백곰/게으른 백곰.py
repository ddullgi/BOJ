import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * 1000001
e = 0
for _ in range(N):
    g, x = map(int, input().split())
    arr[x] = g
    e = max(e, x)

s = 2 * K + 1
tmp = sum(arr[:s])
answer = tmp

for i in range(s, e + 1):
    tmp += arr[i] - arr[i-s]
    answer = max(answer, tmp)
print(answer)