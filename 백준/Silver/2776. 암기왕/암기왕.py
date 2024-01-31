def binary_search(arr, k): 
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == k:
            return 1
        elif arr[mid] < k:
            l = mid + 1
        else:
            r = mid - 1  
    return 0
    
t = int(input())

for _ in range(t):
    n = int(input())
    arr1 = list(map(int,input().split())) 
    m = int(input())
    arr2 = list(map(int,input().split())) 

    arr1 = list(set(arr1)) 
    arr1.sort()

    for x in arr2:
        print(binary_search(arr1, x))