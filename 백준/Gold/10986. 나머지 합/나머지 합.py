import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
s = 0
arr = [0] * M

for i in range(N):
    s += num[i]
    arr[s % M] += 1

result = arr[0]

for i in arr:
    result += i * (i - 1) // 2

print(result)