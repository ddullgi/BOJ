import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())

PrefixSum = [0]
for i in arr:
    PrefixSum.append(PrefixSum[-1] + i)

for _ in range(M):
    s, e = map(int, input().split())
    print(PrefixSum[e] - PrefixSum[s - 1])