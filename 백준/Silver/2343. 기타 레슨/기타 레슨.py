N, M = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
l, r = max(arr), sum(arr)
while l <= r:
    m = (l + r) // 2

    count, s = 0, 0
    for i in range(N):
        if s + arr[i] > m:
            count += 1
            s = 0
        s += arr[i]
    if s:
        count += 1

    if count > M:
        l = m + 1
    else:
        r = m - 1
        answer = m

print(answer)