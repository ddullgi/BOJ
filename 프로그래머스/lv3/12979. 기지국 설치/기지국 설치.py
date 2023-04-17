def solution(n, stations, w):
    answer = 0
    arr = []
    m = 0
    r = w * 2 + 1
    
    for i in stations:
        if i - w > m + 1:
            print(i, m)
            arr.append(i - w - m - 1)
        
        m = i + w
    
    if m < n:
        arr.append(n - m)
    
    for b in arr:
        answer += b // r
        if b % r:
            answer += + 1
        
    return answer