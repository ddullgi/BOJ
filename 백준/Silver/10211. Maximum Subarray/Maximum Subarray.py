T = int(input())

for i in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = [arr[0]]
    
    for i in range(1, n):
        big = max(result[i - 1] + arr[i], arr[i])
        result.append(big)
    print(max(result))