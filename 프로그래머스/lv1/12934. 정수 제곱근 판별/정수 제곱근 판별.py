def solution(n):
    n = n ** 0.5
    answer = int(n + 1) ** 2 if not n - int(n) else -1
    
    return answer