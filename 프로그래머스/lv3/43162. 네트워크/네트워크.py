from collections import deque

def solution(n, computers):
    answer = 0
    visit = [0] * n
    Q = deque()
    
    
    for i in range(n):
        if visit[i] == 1:
            continue
        Q.append(i)
        visit[i] = 1
        while Q:
            d = Q.popleft()
            for i in range(n):
                if computers[d][i] == 1 and visit[i] == 0:
                    Q.append(i)
                    visit[i] = 1
        answer += 1
    
    return answer