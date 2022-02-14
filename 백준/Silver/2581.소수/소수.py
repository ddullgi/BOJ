minN = int(input())
maxN = int(input())


def fun(n):
    arr = [1] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if arr[i] == 1:
            for j in range(i + i, n + 1, i):
                arr[j] = 0
    return [i for i in range(2, n + 1) if arr[i] == 1]


arr1 = fun(maxN)
arr2 = []
for i in arr1:
    if i >= minN:
        arr2 += [i]
if not arr2:
    print(-1)
else:
    print(sum(arr2))
    print(arr2[0])