def solution(n):
    answer = 0
    arr = [1, 2]
    if n < 3:
        return arr[n - 1]
    
    for i in range(2, n):
        arr.append(arr[i - 1] + arr[i - 2])
        
    answer = arr[n - 1] % 1234567
    return answer