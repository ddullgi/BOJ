arr = []
for _ in range(int(input())):
    arr.append(int(input()))
arr.sort(reverse=True)
result = 0
for i in range(len(arr)):
    if (i + 1) % 3 == 0:
        continue
    result += arr[i]

print(result)