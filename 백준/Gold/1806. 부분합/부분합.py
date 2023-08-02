N, M = map(int, input().split())
arr = list(map(int, input().split()))
l = 0
r = 0
result = 100000
temp = arr[0]

while l <= r:
    if temp >= M:
        result = min(result, r - l + 1)
        temp -= arr[l]
        l += 1
    else:
        r += 1
        if r < N:
            temp += arr[r]
        else:
            break

if result == 100000:
    print(0)
else:
    print(result)