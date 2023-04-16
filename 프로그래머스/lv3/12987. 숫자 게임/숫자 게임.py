def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    while B:
        a = A.pop()
        b = B.pop()
        if a >= b:
            while B and B[-1] <= a:
                B.pop()
            if B:
                B.pop()
                answer += 1   
        else:
            answer += 1   
                
    return answer