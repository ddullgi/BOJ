arr = []
maxV = 0
for _ in range(9):
    a = int(input())
    arr += [a]
    maxV += a

for i in range(8,0,-1):
    for j in range(0, i):
        if maxV - arr[i] - arr[j] == 100:
            arr.remove(arr[i])
            arr.remove(arr[j])
            break
    if len(arr) < 9:
        break

for k in range(7,0,-1):
    for l in range(1, k):
        if arr[l-1] > arr[l]:
            arr[l - 1], arr[l] = arr[l], arr[l - 1]

for m in arr:
    print(m)