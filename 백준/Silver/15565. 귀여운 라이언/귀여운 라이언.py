INF = float('inf')

n, k = map(int, input().split())
arr = list(map(int, input().split()))

size, cnt, e = 0, 0, 0
answer = INF

for s in range(n):
    while cnt < k and e < n:
        size += 1
        if arr[e] == 1:
            cnt += 1
        e += 1

    if cnt == k and answer > size:
        answer = size

    if arr[s] == 1:
        cnt -= 1
    size -= 1

print(answer if answer != INF else -1)