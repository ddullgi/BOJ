n = int(input())
arr = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append([a,b])
mid_x = sorted(arr, key=lambda x:x[0])[n//2][0]
mid_y = sorted(arr, key=lambda x:x[1])[n//2][1]

result = 0
for i in arr:
    result += (abs(mid_x - i[0]) + abs(mid_y - i[1]))
print(result)