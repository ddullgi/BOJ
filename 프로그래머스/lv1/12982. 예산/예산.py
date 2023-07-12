def solution(d, budget):
    answer = 0
    d.sort(reverse=True)
    arr = []
    while budget > 0 and d:
        budget -= d.pop()
        answer += 1
    
    answer = answer if budget >= 0 else answer - 1
    
    return answer