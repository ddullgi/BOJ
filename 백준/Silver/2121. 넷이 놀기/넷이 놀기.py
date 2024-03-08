import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
d = [tuple(map(int, input().split())) for _ in range(n)]
d = set(d)

answer = 0

for x, y in d:
    if (x + a, y) in d and (x, y + b) in d and (x + a, y + b) in d:
        answer += 1

print(answer)