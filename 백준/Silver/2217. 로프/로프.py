N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(len(arr)):
    arr[i] = arr[i] * (i + 1)

print(max(arr))