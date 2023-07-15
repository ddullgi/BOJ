N, M = map(int, input().split())
arr = list(map(int, input().split()))

r = max(arr)
l = 0

def cut(x):
    result = 0
    for i in arr:
        if i - x > 0:
            result += i - x

    return result


while l <= r:
    m = (l + r) // 2
    k = cut(m)

    if k >= M:
        l = m + 1
    else:
        r = m - 1

print(r)