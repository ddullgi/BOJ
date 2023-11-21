N, K = map(int, input().split())
arr = [ int(input()) for _ in range(N) ]
s, e = 1, max(arr)
res = 0
while s <= e:
    m = (s + e) // 2
    t = sum(n // m for n in arr)
    if t >= K:
        res = m
        s = m + 1
    else:
        e = m - 1
print(res)