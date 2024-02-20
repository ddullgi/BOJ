n = int(input())
arr = []

for i in range(n):
    arr.append(input())

arr = list(set(arr))
result = 0
for i in range(len(arr)):
    for j in range(len(arr)):
        if len(arr[i]) <= len(arr[j]) and i != j:
            if arr[i] == arr[j][:len(arr[i])]:
                result += 1
                break
            
print(len(arr)-result)