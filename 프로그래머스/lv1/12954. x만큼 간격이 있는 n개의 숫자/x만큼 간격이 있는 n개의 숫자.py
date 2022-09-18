def solution(x, n):
    answer = []
    i = 0
    a = 0
    while i < n:
        a += x
        answer.append(a)
        
        i += 1
    
    return answer