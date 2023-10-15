def dfs(arr, idx):
    if len(arr) == 6:
        for l in arr:
            print(l, end = ' ')
        print()
        return
        
    for i in range(idx, len(lotto)):
        dfs(arr + [lotto[i]], i+1)


while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    lotto = arr[1:]
    dfs([], 0)
    print()