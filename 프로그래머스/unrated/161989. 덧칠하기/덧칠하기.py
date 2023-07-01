from collections import deque 

def solution(n, m, section):
    Q = deque(section)
    cnt = 1
    flag = section[0] + m - 1
    
    while Q:
        if Q[0] <= flag:
            Q.popleft()
        else:
            cnt += 1
            flag = Q[0] + m - 1
            
    return cnt