n, m = map(int, input().split())

arr = []
arr += map(int, input().split())

for _ in range(m):
    arr.sort()
    arr[0] = arr[1] = arr[0] + arr[1]

print(sum(arr))