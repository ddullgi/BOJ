import sys
N = int(sys.stdin.readline())
T = []
result = 0
M = -0xffffffff
for _ in range(N):
    n, m = map(int, sys.stdin.readline().split())
    T.append((n, m))

T.sort(key=lambda x: (x[0], x[1]))

for x, y in T:
    if y < M:
        continue
    else:
        if x > M:
            result += y - x
        else:
            result += y - M
        M = y

print(result)