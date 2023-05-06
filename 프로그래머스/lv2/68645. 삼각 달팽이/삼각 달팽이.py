def solution(n):
    answer = []
    arr = [[0] * n for _ in range(n)]
    y, x = -1, 0
    d = (1, 0)
    i = 1
    while n > 0:
        for _ in range(n):
            y += d[0]
            x += d[1]
            arr[y][x] = i
            i += 1
            
        
        if d == (1, 0):
            d = (0, 1)
        elif d == (0, 1):
            d = (-1, 0)
        elif d == (-1, 0):
            x -= n - 1
            d = (1, 0)
        
        n -= 1
    
    for i in arr:
        for j in i:
            if j != 0:
                answer.append(j)
            
    return answer