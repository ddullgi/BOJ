import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []

for _ in range(N):
    arr.append(int(input()))

arr.sort()

l = 0
r = 1
m = 2000000000
while l <= r and r < N:
    tmp = arr[r] - arr[l]
    
    if tmp < M:
        r += 1
    else:
        l += 1
        m = min(m, tmp)

print(m)