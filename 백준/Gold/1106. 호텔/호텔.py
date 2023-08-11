import sys
input = sys.stdin.readline

C, N = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]
memo = [1e7] * (C + 100)
memo[0] = 0

for cost, num_people in arr:
    for i in range(num_people,C+100):
        memo[i] = min(memo[i-num_people]+cost,memo[i])

print(min(memo[C:]))