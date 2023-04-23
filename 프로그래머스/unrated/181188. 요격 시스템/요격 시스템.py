def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1],reverse=True)
    S, E = targets[0]
    for s, e in targets:
        if S >= e:
            S = s
            answer += 1
        elif S < s:
            S = s
        E = e
    answer += 1
        
    return answer