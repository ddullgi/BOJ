from collections import deque

def solution(x, y, n):
    Q = deque()
    Q.append(x)
    d = {x: 0}
    answer = -1
    
    if x == y:
        return 0
    
    while Q:
        dx = Q.popleft()
        if dx == y:
            break
        
        for nx in [dx + n, dx * 2, dx * 3]:
            if not d.get(nx) and nx <= y:
                d[nx] = d[dx] + 1
                Q.append(nx)
    
    if d.get(y):
        answer = d[y]
        
    
    return answer