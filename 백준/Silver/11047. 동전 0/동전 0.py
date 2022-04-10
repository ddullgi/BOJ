N, K = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(int(input()))

cnt = 0
for i in range(N - 1, -1, -1):
    while K >= lst[i]:
        K -= lst[i]
        cnt += 1

print(cnt)