def solution(s):
    d = {}
    answer = []
    
    for i in range(1, len(s) + 1):
        if d.get(s[i - 1]):
            answer.append(i - d[s[i - 1]])
        else:
            answer.append(-1)
        d[s[i - 1]] = i
        
    return answer