def solution(sizes):
    maxL = 0
    minL = 0
    
    for i, j in sizes:
        if i >= j:
            maxL = max(i, maxL)
            minL = max(j, minL)
        else:
            maxL = max(j, maxL)
            minL = max(i, minL)
            
    return maxL * minL