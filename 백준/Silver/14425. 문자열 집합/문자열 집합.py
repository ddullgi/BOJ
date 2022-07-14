N, M = map(int, input(). split())
S = set()
for _ in range(N):
    S.add(input())

cnt = 0
for i in range(M):
    if input() in S:
        cnt += 1
print(cnt)