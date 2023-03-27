def solution(routes):
    routes.sort(key=lambda x: x[0])
    
    answer = 0
    E = -30000
    for s, e in routes:
        if s > E:
            print(E)
            answer += 1
            E = e
        E = min(E, e)
    return answer