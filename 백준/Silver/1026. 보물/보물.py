n = int(input())

arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

s = 0
for i in range(n):
    s += min(arr) * max(arr2)
    arr.pop(arr.index(min(arr)))
    arr2.pop(arr2.index(max(arr2)))

print(s)