n, m = map(int, input().split())
arr = []
arr2 = []

for _ in range(m):
    a, b = map(int, input().split())
    arr.append(a)
    arr2.append(b)

min_arr = min(arr)

ans = 0
while n > 0:
    if n >= 6:
        min_arr2 = min(arr2)*6
        n -= 6
    else:
        min_arr2 = min(arr2)*n
        n -= n
    if min_arr2 < min_arr:
        ans += min_arr2
    else:
        ans += min_arr

print(ans)