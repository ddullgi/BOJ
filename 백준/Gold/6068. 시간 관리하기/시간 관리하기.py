N = int(input())
arr = []
for _ in range(N):
    A, B = map(int, input().split())
    arr.append((B, A))

arr.sort(reverse=True)
_max = arr[0][0]
for i in range(N):
    if arr[i][0] < _max:
        _max = arr[i][0]

    _max -= arr[i][1]

    if _max < 0:
        break

if _max < 0:
    print(-1)
else:
    print(_max)