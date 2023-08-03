import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

PrefixSum = [0]
for i in arr:
    PrefixSum.append(PrefixSum[-1] + i)

for _ in range(M):
    s, e = map(int, input().split())
    print(PrefixSum[e] - PrefixSum[s - 1])