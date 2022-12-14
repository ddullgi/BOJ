N = int(input())
arr = list(map(int, input().split()))
arr.sort()

L = 0
R = len(arr) - 1
_min = 0xffffffff
result_L, result_R = arr[L], arr[R]

while L < R:
    _sum = arr[L] + arr[R]

    if abs(_min) > abs(_sum):
        result_L, result_R = arr[L], arr[R]
        _min = _sum

    if _sum > 0:
        R -= 1
    elif _sum < 0:
        L += 1
    else:
        break

print(result_L, result_R)